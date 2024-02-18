import json
import queue
import traceback
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from typing import Dict, List, Optional, Union

import ijson
from langchain_core.messages import HumanMessage, BaseMessage, get_buffer_string
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate

from lemon_rag.dependencies.data_access import data_access
from lemon_rag.lemon_runtime import models
from lemon_rag.llm.callback_handlers.form_callback_handler import JSONLineCallbackHandler
from lemon_rag.llm.callback_handlers.io_utils import StringChannel
from lemon_rag.llm.client.base_client import ChatChain
from lemon_rag.protocols.business_form import get_form_schema_by_type
from lemon_rag.protocols.chat import SelectSettings, ResponseChunk, FormKVPair, DatetimeSettings, \
    FormSchema, CardMessage, FormComponent, FormData, BusinessDataType, CallbackMethod, FormFieldSchema, \
    FormControlComponent, ClickAction, MoneySettings
from lemon_rag.utils import log
from lemon_rag.utils.executor_utils import submit_task

json_parser_pool = ThreadPoolExecutor(max_workers=10)

system_message_template = """
# Role
Your duty is extract json data from the user's input.

# Context
Now it is {date} today.

# Current Form Schema
you need to extract lines of json data satisfies the following schema.
{schema}

# Tips
* You are preferred split the user's input in to as more record as possible.
* You can infer and fill in missing fields based on the existing fields, such as employee gender.

# Output
You need extract data and output them in the format of jsonline.
If the user missed any information, you can leave the respective fields empty or deduce the most possible value of the field.

The chat history is:
{history}

"""


def format_form_schema(form_schema: FormSchema) -> str:
    form_fields_format: Dict = {}
    for form_field in form_schema.fields:
        if isinstance(form_field.field_settings, SelectSettings):
            if form_field.field_settings.options:
                form_field_value = f"{'|'.join([option.label for option in form_field.field_settings.options])}"
            elif form_field.field_settings.multiple:
                form_field_value = "values split by ,"
            else:
                form_field_value = ""
        elif isinstance(form_field.field_settings, DatetimeSettings):
            form_field_value = "%Y年%m月%d日"
        elif isinstance(form_field.field_settings, MoneySettings):
            form_field_value = "a number can be parsed by python decimal.Decimal"
        else:
            form_field_value = ""
        form_fields_format[form_field.name] = form_field_value
    return json.dumps(form_fields_format, ensure_ascii=False)


def process_json_fragment(
        q: queue.Queue,
        string_channel_q: queue.Queue,
        message: Optional[models.MessageTab],
        card: CardMessage,
        schema: FormSchema,
        timeout: int = 15
):
    session_id: int = 0
    msg_id: int = 0
    if message:
        session_id = message.session.id
        msg_id = message.msg_id
    first_json = True
    while True:
        try:
            string_channel: Union[StringChannel, str] = string_channel_q.get(timeout=timeout)
        except queue.Empty:
            log.info("try to get string channel, but queue is empty")
            continue
        log.info("got string channel [%s]", string_channel)
        if isinstance(string_channel, str):
            break
        if first_json:
            q.put(
                ResponseChunk.add_text(
                    session_id,
                    msg_id,
                    f"请确认以下`{schema.type.value}`表单的信息，确认无误后点击`提交`完成记录。",
                    card
                ).json()
            )
            first_json = False

        # 收到json 推送schema
        name_to_field_mapping: Dict[str, FormFieldSchema] = {f.name: f for f in schema.fields}
        form = FormComponent(data=FormData(form_schema=schema))
        q.put(ResponseChunk.add_form(session_id, msg_id, form, card).json())
        data_map = {}

        def push_kv_pair(k: str, v: Optional[str]):
            field_schema = name_to_field_mapping.get(k)

            if not field_schema:
                return

            v = v or field_schema.get_default_value()

            q.put(ResponseChunk.set_form_data(
                session_id, msg_id, form, [FormKVPair(key=k, value=v)]).json())
            data_map[k] = v
            if field_schema.control_component != FormControlComponent.SELECT:
                return

            if field_schema.field_settings.options:
                return
            log.info("update select field schema: %s", field_schema.json())
            field_schema.field_settings.options_params.keyword = v
            q.put(ResponseChunk.update_field_schema(session_id, msg_id, form.id, field_schema).json())

        try:
            for key, value in ijson.kvitems(string_channel, ''):
                log.info(f"extracted key=[%s] value=[%s]", key, value)
                push_kv_pair(key, value)
        except Exception as e:
            log.info("parse json line error: %s", traceback.format_exc())

        for field in schema.fields:
            if field.name not in data_map:
                push_kv_pair(field.name, field.get_default_value())
    # 按钮
    if not first_json:
        button_callbacks: List[CallbackMethod] = [
            CallbackMethod.handle_form(schema.type.api_sub_path()),
            CallbackMethod.update_button(session_id, msg_id, ClickAction.after_form_submit)
        ]
        q.put(ResponseChunk.add_button(session_id, msg_id, "提交", button_callbacks, card).json())
        return
    q.put(ResponseChunk.add_text(session_id, msg_id, "好的，请给我提供具体信息，我将为你记录。", card).json())


def form_record_chat(
        histories: List[BaseMessage],
        raw_form_schema: FormSchema,
        ai_message: models.MessageTab,
        q: queue.Queue,
        card: CardMessage
) -> str:
    chat_chain = ChatChain(template=ChatPromptTemplate.from_strings(
        [
            (SystemMessagePromptTemplate, system_message_template),
            HumanMessage(content="You have got enough information. Please output the result now.")
        ])
    )

    formatted_history = get_buffer_string(histories)
    log.info("%s", {
        "schema": format_form_schema(raw_form_schema),
        "date": datetime.now().strftime("%Y年%m月%d日"),
        "history": formatted_history
    })

    string_channel_q = queue.Queue(maxsize=8)

    aigc_future = submit_task(json_parser_pool, chat_chain.run, **{
        "callbacks": [JSONLineCallbackHandler(q=string_channel_q)],
        "schema": format_form_schema(raw_form_schema),
        "date": datetime.now().strftime("%Y年%m月%d日"),
        "history": formatted_history
    })

    process_json_fragment(q, string_channel_q, ai_message, card, raw_form_schema, timeout=10)
    aigc_future = aigc_future.result()
    print(aigc_future)
    if ai_message:
        log.info("card: %s", card)
        log.info("card_json: %s", card.json)
    return aigc_future


if __name__ == '__main__':
    q = queue.Queue()
    card = CardMessage()
    form_record_chat(
        [HumanMessage(content="新造地铁合同A001有两个应收单，一个是采购电梯材料，一个是采购点提升将带子")],
        get_form_schema_by_type(BusinessDataType.receivable_payable),
        None,
        q,
        card
    )
    while not q.empty():
        print(q.get())
    print(card)
