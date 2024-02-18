import datetime
import json
import queue
from typing import List, Optional, Union

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, AIMessage, FunctionMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate

from lemon_rag.dependencies.data_access import data_access
from lemon_rag.lemon_runtime import models
from lemon_rag.llm.agents.interactive_functions import form_record
from lemon_rag.llm.agents.interactive_functions.base_function import ToolFunction
from lemon_rag.llm.agents.interactive_functions.data_query_functions import QueryOrAnalysisData
from lemon_rag.llm.agents.interactive_functions.form_record import CreateNewEmployee, CreateNewProject, \
    CreatePaymentAccount, RecordInternalTransfer, CreateNewContract, RecordAdvanceBill
from lemon_rag.llm.agents.rag.vectorization.runner import vectorization_pool, vectorize_message
from lemon_rag.llm.callback_handlers.text_callback_handler import TextCallbackHandler
from lemon_rag.llm.client.base_client import ChatChain
from lemon_rag.protocols.chat import CardMessage
from lemon_rag.utils import log
from lemon_rag.utils.api_utils import send_base_message, get_send_text_message_function
from lemon_rag.utils.executor_utils import submit_task

system_message_template = """
# Role
You are an AI personal assistant. 
Your responsibility is to assist user to manage the construction projects. 
you need to call the functions provided to record business data or perform some complex queries.

# Rules
* You are preferred to chat with the user using Chinese.
* You must call the respective function to record the data or query the data before you give a response to the user.

# Output Tips
User Input:
帮我记一下xxx项目从xx采购了xxx，花了xxx元已经付完钱了
AI:
call `RecordTransaction`

User Input:
刚刚给xx付了昨天的奶茶钱
AI:
call `RecordTransaction`

User Input:
帮我记一下xxx项目从xx采购了xx，一共是xxx元下个月一号结账
AI:
call `RecordReceivablePayableBill`

User Input:
xxx项目有xx元是质量保证金，项目完事儿后2个月内付。
AI:
call `RecordReceivablePayableBill`

User Input:
xxx项目下周他先付xx元，等做到xxx阶段再付剩下的xx元。
AI:
call `RecordReceivablePayableBill`

Now it is {datetime}, please assist the user based on the rules above.
"""


def form_record_or_query(
        user_input: str,
        histories: List[BaseMessage],
        user_message: Optional[models.MessageTab],
        ai_message: Optional[models.MessageTab],
        summarization: Optional[BaseMessage],
        q: queue.Queue
) -> str:
    log.info("executing form_record_or_query, user_input=%s", user_input)
    callbacks = []
    session_id = 0
    msg_id = 0
    card = CardMessage(components=[])
    if ai_message:
        send_base_message(user_message, ai_message, q)
        session_id = ai_message.session.id
        msg_id = ai_message.msg_id
        card = CardMessage.parse_raw(ai_message.content)
        send_text_message_func = get_send_text_message_function(q, session_id, msg_id, card)
        callbacks.append(TextCallbackHandler(send_text_message_func))
    chat_chain = ChatChain(
        template=ChatPromptTemplate.from_strings(
            [(SystemMessagePromptTemplate, system_message_template)] +
            ([SystemMessage(content=summarization.content)] if summarization else [])
            + histories + [HumanMessage(content=user_input)]
        ),
        functions=[
            form_record.CreateNewEmployee,
            form_record.CreateNewProject,
            form_record.CreatePaymentAccount,
            form_record.RecordInternalTransfer,
            form_record.CreateNewContract,
            form_record.CreateNewInvoice,
            form_record.RecordTransaction,
            form_record.RecordSalaryBill,
            form_record.RecordReceivablePayableBill,
            form_record.RecordAdvanceBill,
            form_record.CreateNewSupplier,
            form_record.CreateNewCustomer,
            QueryOrAnalysisData
        ]
    )

    log.info(chat_chain.template.format(**{"datetime": datetime.datetime.now().strftime("%Y年%m月%d日")}))

    result = chat_chain.run(
        callbacks=callbacks,
        datetime=datetime.datetime.now().strftime("%Y年%m月%d日")
    )

    log.info(
        f"ai generate: {result}, 类型：{type(result)}, 属于tool_function类型: {isinstance(result, ToolFunction)}")

    if isinstance(result, ToolFunction):
        function_call = {
            "name": result.__class__.__name__,
            "arguments": result.json(by_alias=True)
        }
        messages: List[Union[AIMessage, FunctionMessage]] = [
            AIMessage(content="", additional_kwargs={"function_call": function_call}),
            FunctionMessage(name=result.__class__.__name__, content="执行完成")
        ]  # TODO: 把context text的更新放在function call完成之后，根据function call的结果
        data_access.update_message_content_text_context_text(
            msg_id, card.json(),
            json.dumps([m.dict() for m in messages]),
            json.dumps([m.dict() for m in messages]),
            ai_message.session
        )
        res = result.execute(q, ai_message, user_input, card)
        data_access.update_message_content(ai_message.msg_id, card.json(), ai_message.session)
        return res
    # 将消息组件作为倒排索引录入向量数据库
    submit_task(vectorization_pool, vectorize_message, user_message, CardMessage.parse_raw(user_message.content))
    submit_task(vectorization_pool, vectorize_message, ai_message, card)
    data_access.update_message_content_text_context_text(msg_id, card.json(), result, result, ai_message.session)
    return result


if __name__ == '__main__':
    q = queue.Queue(maxsize=1000)
    form_record_or_query(
        "李老板家项目开工前一周他先付10w，水电木工做完付10w，现场清理完毕后再付10w，最后10w保证金项目完事后2个月内付",
        [],
        None,
        None,
        None,
        q
    )
