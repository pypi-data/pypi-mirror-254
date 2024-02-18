import datetime
import hashlib
import hmac
import json
import urllib.parse
import base64
import queue
from typing import Optional, List, Dict, Type, Union

import peewee
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, SystemMessage, FunctionMessage
from playhouse.shortcuts import model_to_dict

from lemon_rag.dependencies.data_access import data_access, business_data_access
from lemon_rag.dependencies.vector_access import CandidateSearchRes
from lemon_rag.lemon_runtime import models, wrappers
from lemon_rag.llm.agents.rag.vectorization.runner import vectorization_pool, vectorize_message
from lemon_rag.protocols.business_form import get_form_schema_by_type
from lemon_rag.protocols.chat import ResponseChunk, CompleteMessage, CardMessage, RefFile, CallbackMethod, \
    CardCallbackAction, ClickAction, ChatRole, CardComponentType, BusinessType, Form, OptionPair, Dependency, \
    BusinessDataType, DependencyType
from lemon_rag.utils import log
from lemon_rag.utils.executor_utils import submit_task


def get_xunfei_auth_url(url: str, api_secret: str, api_key: str) -> str:
    parsed_url = urllib.parse.urlparse(url)
    # 签名时间
    date = datetime.datetime.now(datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
    # 参与签名的字段 host, date, request-line
    sign_string = [
        f'host: {parsed_url.hostname}',
        f'date: {date}',
        f'GET {parsed_url.path} HTTP/1.1'
    ]
    # 拼接签名字符串
    sign = '\n'.join(sign_string)
    # 签名结果
    sha = hmac.new(api_secret.encode(), sign.encode(), hashlib.sha256).digest()
    signature = base64.b64encode(sha).decode()
    # 构建请求参数，此时不需要 URL 编码
    auth_url = f'api_key="{api_key}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature}"'
    # 将请求参数使用 base64 编码
    authorization = base64.b64encode(auth_url.encode()).decode()
    query_params = urllib.parse.parse_qs(parsed_url.query)
    query_params['host'] = [parsed_url.hostname]
    query_params['date'] = [date]
    query_params['authorization'] = [authorization]
    # 将编码后的字符串 URL 编码后添加到 URL 后面
    final_url = url + '?' + urllib.parse.urlencode(query_params, doseq=True)
    return final_url


def send_base_message(user_message: Optional[models.MessageTab], ai_message: models.MessageTab, q: queue.Queue):
    if user_message:
        user_msg_dict = model_to_dict(user_message)
        log.info("user_msg_dict=%s", user_msg_dict)
        q.put(ResponseChunk.base_message(
            user_message.session.id,
            user_message.msg_id,
            CompleteMessage(**user_msg_dict)
        ).json())
    q.put(ResponseChunk.base_message(
        ai_message.session.id,
        ai_message.msg_id,
        CompleteMessage(**model_to_dict(ai_message))
    ).json())


def upload_file_in_chat(
        user_message: Optional[models.MessageTab],
        ai_message: models.MessageTab,
        file: models.FileTab,
        kb: models.KnowledgeBaseTab,
        q: queue.Queue
):
    user_card = CardMessage.parse_raw(user_message.content)
    user_card.components = []
    signed_url = wrappers.lemon.utils.oss_bucket.sign_url(file.path)
    ref_file = RefFile(
        id=file.id, origin_filename=file.name, url=signed_url, extension=file.extension, file_size=file.size)
    user_card.add_file(ref_file)
    data_access.update_message_content_text_context_text(
        user_message.msg_id,
        user_card.json(), f"用户上传了文件: {file.name}", f"用户上传了文件: {file.name}", user_message.session)
    user_message = data_access.get_message_by_msg_id(user_message.msg_id, user_message.session)
    data_access.update_message_support_retry(user_message.msg_id, False, user_message.session)

    send_base_message(user_message, ai_message, q)

    card = CardMessage.parse_raw(ai_message.content)
    q.put(ResponseChunk.add_text(
        ai_message.session.id, ai_message.msg_id, f"你将对文件`{file.name}`做以下操作：", card).json())
    q.put(ResponseChunk.add_file(ai_message.session.id, ai_message.msg_id, ref_file, card).json())

    session = data_access.get_session_by_id(ai_message.session.id)
    if session.role == ChatRole.standard_query:
        callbacks = [
            CallbackMethod(
                action=CardCallbackAction.UPLOAD_KNOWLEDGE_BASE_FILE,
                params={"file_id": file.id, "filename": file.name, "knowledge_base_id": kb.id}
            ),
            CallbackMethod(
                action=CardCallbackAction.CLICK_BUTTON_EVENT,
                params={"msg_id": ai_message.msg_id, "session_id": ai_message.session.id,
                        "action": ClickAction.after_upload_knowledgebase_file}
            ),
        ]
        q.put(ResponseChunk.add_button(
            ai_message.session.id, ai_message.msg_id, "上传知识库", callback=callbacks, card=card).json())
    if session.role == ChatRole.assistant:
        q.put(ResponseChunk.add_button(
            ai_message.session.id, ai_message.msg_id, "内容识别", callback=[], card=card).json())
    data_access.update_message_content_text_context_text(
        ai_message.msg_id, card.json(),
        f"文件: {file.name}正在处理中...", f"文件: {file.name}正在处理中...", ai_message.session)
    data_access.update_message_support_retry(ai_message.msg_id, False, ai_message.session)

    # 将消息组件作为倒排索引录入向量数据库
    submit_task(vectorization_pool, vectorize_message, user_message, user_card)
    submit_task(vectorization_pool, vectorize_message, ai_message, card)


def get_send_text_message_function(q: queue.Queue, session_id: int, msg_id: int, card: CardMessage):
    def send(text: str, append: bool = True):
        q.put(ResponseChunk.add_text(session_id, msg_id, text, card, append).json())

    return send


def get_chat_context_history(
        session: models.SessionTab, context_length: int = 10, text_only: bool = False
) -> List[BaseMessage]:
    messages: List[BaseMessage] = []
    raw_messages = data_access.get_last_message_by_session_id(session, context_length)
    for raw_message in raw_messages[::-1]:

        if text_only:
            # 如果不是纯文字消息就停止
            card = CardMessage.parse_raw(raw_message.content)
            log.info('[get chat history] %s', raw_message)
            log.info(
                "filter text only messages %s %s %s",
                (not card.components),
                bool(card.components),
                (len(card.components) != 1 or card.components[0].type != CardComponentType.TEXT)
            )
            if not card.components:
                continue
            if card.components and (len(card.components) != 1 or card.components[0].type != CardComponentType.TEXT):
                break

        if raw_message.role == ChatRole.assistant:
            try:
                context_text = json.loads(raw_message.context_text)
            except json.decoder.JSONDecodeError:
                context_text = raw_message.context_text
            if isinstance(context_text, list):
                ai_message, function_message = context_text
                messages.append(AIMessage(**ai_message))
                messages.append(FunctionMessage(**function_message))
            else:
                messages.append(AIMessage(content=raw_message.context_text))
        if raw_message.role == ChatRole.user:
            messages.append(HumanMessage(content=raw_message.context_text))
    return messages[::-1]


def get_summarization_context_history(session: models.SessionTab, context_length: int = 10) -> List[BaseMessage]:
    summarizations: List[BaseMessage] = []
    raw_summarizations = data_access.get_last_summarization_by_session_id(session, context_length)
    for raw_summarization in raw_summarizations:
        summarizations.append(SystemMessage(content=raw_summarization.summarization))
    return summarizations


def get_business_db_cls_by_type(type_: BusinessType) -> Type[peewee.Model]:
    business_type_to_db_cls: Dict[BusinessType, Type[peewee.Model]] = {
        BusinessType.transaction_item: models.TransactionItemTab,
        BusinessType.contract: models.ContractTab,
        BusinessType.receivable_payable: models.ReceivablePayableTab,
        BusinessType.employee_loan: models.EmployeeLoanTab,
        BusinessType.salary: models.SalaryTab,
        BusinessType.supplier: models.SupplierTab,
        BusinessType.customer: models.CustomerTab,
        BusinessType.employee: models.EmployeeTab,
        BusinessType.project: models.ProjectTab,
        BusinessType.account: models.AccountTab
    }
    return business_type_to_db_cls.get(type_)


def list_combobox_candidate_from_db_by_type(
        type_: BusinessType, creator: models.AuthUserTab) -> List[CandidateSearchRes]:
    data_list = business_data_access.list_data_by_cls_creator(get_business_db_cls_by_type(type_), creator, [])
    if type_ in [BusinessType.receivable_payable, BusinessType.salary, BusinessType.employee_loan]:
        return [CandidateSearchRes(vectorization_key=data.description, business_id=data.id) for data in data_list]
    else:
        return [CandidateSearchRes(vectorization_key=data.name, business_id=data.id) for data in data_list]


def get_combobox_candidate_from_db_by_id_dependencies(
        type_: BusinessType, id_: int, dependencies: List[Dependency], creator: models.AuthUserTab
) -> Optional[OptionPair]:
    dependencies_name_data_mapping: Dict[str, Union[peewee.Model, str, bool]] = {}
    for dep in dependencies:
        if dep.dependency_type == DependencyType.CONST:
            dependencies_name_data_mapping[getattr(dep.type, "name", None) or dep.name] = dep.value
            continue
        data = business_data_access.get_data_by_cls_id(get_business_db_cls_by_type(dep.type), dep.value, creator)
        dependencies_name_data_mapping[getattr(dep.type, "name", None) or dep.name] = data
    if dependencies:
        data = business_data_access.get_data_by_cls_id_dependencies(
            get_business_db_cls_by_type(type_), id_, dependencies_name_data_mapping, creator)
    else:
        data = business_data_access.get_data_by_cls_id(get_business_db_cls_by_type(type_), id_, creator)
    if not data:
        return None
    if type_ in [BusinessType.receivable_payable, BusinessType.salary, BusinessType.employee_loan]:
        description = f"{data.employee.name}+{data.date}+{data.description}"
        return OptionPair(label=description, value=data.id)
    else:
        return OptionPair(label=data.name, value=data.id)


def update_message_after_save_form(msg_id: int, session_id: int, forms: List[Form]):
    id_form_mapping = {form.id: form for form in forms}
    session = data_access.get_session_by_id(session_id)
    message = data_access.get_message_by_msg_id(msg_id, session)
    card = CardMessage.parse_raw(message.content)
    for component in card.components:
        if component.type == CardComponentType.FORM:
            form = id_form_mapping.get(component.id)
            if not form:
                continue
            component.data.submitted = True
            component.data.filled_data = form.data
    data_access.update_message_content(msg_id, card.json(), session)
