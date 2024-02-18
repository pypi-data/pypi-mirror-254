import time
import base64
from functools import partial
from io import StringIO
from typing import List, Optional

from playhouse.shortcuts import model_to_dict
from pydantic import BaseModel, Field

from concurrent.futures import ThreadPoolExecutor
from lemon_rag.api.base import handle_request_with_pydantic, add_route, handle_chat_auth
from lemon_rag.api.local import get_user
from lemon_rag.configs.api_config import runtime_config
from lemon_rag.core.executor_pool import submit_callback_task
from lemon_rag.dependencies.data_access import data_access, KnowledgeBasePermission, GetHistoryType
from lemon_rag.lemon_runtime import models, wrappers
from lemon_rag.llm.agents.prompts.ai_assistent_agent import form_record_or_query
from lemon_rag.llm.agents.prompts.standard_query_agent import default_rag_chat
from lemon_rag.llm.agents.prompts.summarize import generate_summarize_task
from lemon_rag.llm.agents.rag.retrieval.retrieve_messages import retrieve_messages
from lemon_rag.llm.agents.rag.retrieval.retrive_knowledgebase import retrieve_related_paragraphs
from lemon_rag.llm.agents.rag.vectorization.content_extractor import get_extractor, EmptyFile
from lemon_rag.llm.agents.rag.vectorization.runner import start_parse_document
from lemon_rag.protocols.chat import ChatRole, Session, KnowledgeBase, Message, File, SearchHistory, Paragraph, \
    CardMessage, ResponseChunk, CompleteMessage, ClickAction, CardComponentType, RatingType
from lemon_rag.utils import log
from lemon_rag.utils.api_utils import get_xunfei_auth_url, upload_file_in_chat, get_chat_context_history, \
    get_summarization_context_history
from lemon_rag.utils.executor_utils import submit_task
from lemon_rag.utils.file_utils import get_file_hash
from lemon_rag.utils.response_utils import response, ErrorCodes, stream, file_stream

chat_summarization_pool = ThreadPoolExecutor(max_workers=10)


class ListSessionRequest(BaseModel):
    version: int


class ListSessionResponse(BaseModel):
    up_to_date: bool = False
    sessions: Optional[List[Session]] = None


@handle_chat_auth
@handle_request_with_pydantic(ListSessionRequest)
def list_session(req: ListSessionRequest):
    assistant_session, _ = data_access.get_or_create_session(get_user(), ChatRole.assistant)
    notification_session, _ = data_access.get_or_create_session(get_user(), ChatRole.notification_center)
    standard_query, _ = data_access.get_or_create_session(get_user(), ChatRole.standard_query)
    return response(data=ListSessionResponse(sessions=[
        Session(**model_to_dict(assistant_session)),
        Session(**model_to_dict(standard_query)),
        Session(**model_to_dict(notification_session)),
    ]))


class GetNotificationCountRequest(BaseModel):
    version: int


class GetNotificationCountResponse(BaseModel):
    version: int
    unread_count: int


@handle_chat_auth
@handle_request_with_pydantic(GetNotificationCountRequest)
def get_notification_count(req: GetNotificationCountRequest):
    notification_session, _ = data_access.get_or_create_session(get_user(), ChatRole.notification_center)
    sync_history: models.SyncHistoryTab = notification_session.sync_history.get()
    return response(data=GetNotificationCountResponse(
        version=notification_session.version,
        unread_count=(notification_session.last_msg_id or 0) - (sync_history.last_read_id or 0)
    ))


class ReadNotificationsRequest(BaseModel):
    msg_id: int


@handle_chat_auth
@handle_request_with_pydantic(ReadNotificationsRequest)
def read_notifications(req: ReadNotificationsRequest):
    notification_session, _ = data_access.get_or_create_session(get_user(), ChatRole.notification_center)

    data_access.read_message(notification_session, read_id=req.msg_id)
    return response()


class ListKnowledgeFileRequest(BaseModel):
    knowledge_base_id: int


class ListKnowledgeFilesResponse(BaseModel):
    file: List[File]


@handle_chat_auth
@handle_request_with_pydantic(ListKnowledgeFileRequest)
def list_knowledge_base_file(request: ListKnowledgeFileRequest):
    knowledge_base = data_access.get_knowledge_base_by_id(request.knowledge_base_id)
    if not knowledge_base:
        return response(data=ErrorCodes.knowledge_base_not_found)
    knowledge_base_files = data_access.list_knowledge_file_by_knowledge_base(knowledge_base)
    file_list: List[File] = []
    for knowledge_base_file in knowledge_base_files:
        file = data_access.get_file_by_knowledge_base_file(knowledge_base_file)
        if not file:
            continue
        file_list.append(File(**model_to_dict(file)))
    return response(data=ListKnowledgeFilesResponse(file=file_list))


class DeleteKnowledgeFileRequest(BaseModel):
    file_id: int


@handle_chat_auth
@handle_request_with_pydantic(DeleteKnowledgeFileRequest)
def delete_knowledge_base_file(request: DeleteKnowledgeFileRequest):
    delete_num = data_access.delete_knowledge_base_file_link_by_file_id(request.file_id, get_user())
    if delete_num:
        return response()
    return response(code=ErrorCodes.database_operation_error)


class UploadKnowledgeFileRequest(BaseModel):
    file_id: Optional[int]
    file_content: Optional[str]
    filename: str
    knowledge_base_id: int


class UploadKnowledgeFilesResponse(BaseModel):
    file_id: int
    knowledge_base_file_id: int
    filename: str
    file_path: str


def extract_extension(filename: str) -> str:
    return filename.split('.')[-1]


@handle_chat_auth
@handle_request_with_pydantic(UploadKnowledgeFileRequest)
def upload_knowledge_base_file(req: UploadKnowledgeFileRequest):
    if req.file_id and (file := data_access.get_file_by_id_user(req.file_id, get_user())):
        oss_file = wrappers.file_system.create_file(b'', file.content_hash, url=file.path)
        oss_file.load()
        file_content: bytes = oss_file.body
    else:
        file_content: bytes = base64.b64decode(req.file_content)
    file_size: int = len(file_content)
    extension = extract_extension(req.filename).lower()
    # check file basic
    if file_size <= 0:
        return response(code=ErrorCodes.empty_file)
    if file_size >= runtime_config.max_file_bytes:
        return response(code=ErrorCodes.file_size_exceeded)
    if extension not in runtime_config.supported_knowledge_file_types:
        return response(code=ErrorCodes.file_extension_invalid)

    # check kb existence
    kb = data_access.get_knowledge_base_by_id(req.knowledge_base_id)
    if not kb:
        log.info("knowledge base not found, id=%s", req.knowledge_base_id)
        return response(code=ErrorCodes.knowledge_base_not_found)

    # check access
    access = data_access.get_knowledge_base_access(get_user(), kb)
    if not access:
        log.info("no access found for the knowledge_base=%s", kb)
        return response(code=ErrorCodes.permission_denied)

    if not (access.permission & KnowledgeBasePermission.write):
        log.info(
            "the user has permission=%s, but permission=%s required",
            access.permission,
            KnowledgeBasePermission.write
        )
        return response(code=ErrorCodes.permission_denied)

    #
    if data_access.get_knowledge_base_file_count(kb) >= kb.max_files:
        return response(code=ErrorCodes.file_count_exceeded)

    # check hash
    file_hash = get_file_hash(file_content)
    file, is_create_file = data_access.upload_file_by_hash(get_user(), file_hash, kb)
    if file:
        return response(data=UploadKnowledgeFilesResponse(
            file_id=file.id, knowledge_base_file_id=file.knowledge_base_file.id, filename=file.name,
            file_path=file.path))

    oss_file = wrappers.file_system.create_file(file_content, file_hash)
    oss_file.save()
    log.info("upload file, filename=%s, uploaded path=%s", req.filename, oss_file.url)
    knowledge_file, file = data_access.create_knowledge_file(
        oss_file.url, extension, req.filename, file_size, file_hash, is_create_file, kb, get_user())

    buf = StringIO(file_content.decode("utf-8"))
    extractor = get_extractor(extension)
    if not extractor:
        return response(code=ErrorCodes.file_extension_invalid)
    try:
        paragraphs = extractor.extract_content(buf)
    except EmptyFile:
        return response(code=ErrorCodes.pdf_invalid)
    log.info("extracted paragraphs count=%s from %s", len(paragraphs), req.filename)
    start_parse_document(knowledge_file, paragraphs)
    return response(data=UploadKnowledgeFilesResponse(
        file_id=file.id, knowledge_base_file_id=knowledge_file.id, filename=file.name, file_path=file.path))


class FileProcessProgressRequest(BaseModel):
    file_id: int


class FileProcessProgressResponse(BaseModel):
    id: int
    total_parts: int
    vectorized_parts: int


@handle_chat_auth
@handle_request_with_pydantic(FileProcessProgressRequest)
def file_process_progress(request: FileProcessProgressRequest):
    file = data_access.get_knowledge_file_by_id(request.file_id)
    if not file:
        return response(code=ErrorCodes.file_not_found)
    return response(data=FileProcessProgressResponse(**model_to_dict(file)))


class ListKnowledgeBasesRequest(BaseModel):
    version: int


class ListKnowledgeBasesResponse(BaseModel):
    knowledge_bases: List[KnowledgeBase]


@handle_chat_auth
@handle_request_with_pydantic(ListKnowledgeBasesRequest)
def list_knowledge_bases(req: ListKnowledgeBasesRequest):
    knowledge_bases = data_access.list_knowledge_base_by_user(get_user())
    return response(data=ListKnowledgeBasesResponse(knowledge_bases=[
        KnowledgeBase(id=knowledge_base.id, name=knowledge_base.name) for knowledge_base in knowledge_bases]))


class DeleteKnowledgeBasesRequest(BaseModel):
    knowledge_base_id: int


@handle_chat_auth
@handle_request_with_pydantic(DeleteKnowledgeBasesRequest)
def delete_knowledge_bases(req: DeleteKnowledgeBasesRequest):
    knowledgebase = data_access.get_knowledge_base_by_id(req.knowledge_base_id)
    if not knowledgebase:
        return response(code=ErrorCodes.knowledge_base_not_found)
    delete_num = data_access.delete_knowledge_base_by_id_user(req.knowledge_base_id, get_user())
    if delete_num:
        return response()
    return response(data=ErrorCodes.database_operation_error)


class CreateKnowledgeBasesRequest(BaseModel):
    name: str
    max_files: int = 100


class CreateKnowledgeBasesResponse(BaseModel):
    knowledge_base: KnowledgeBase


@handle_chat_auth
@handle_request_with_pydantic(CreateKnowledgeBasesRequest)
def create_knowledge_bases(request: CreateKnowledgeBasesRequest):
    exist_kb = data_access.get_knowledge_base_by_name(request.name, get_user())
    if exist_kb:
        return response(data=ErrorCodes.knowledge_base_existed)
    new_kb = data_access.create_knowledge_base(get_user(), request.name, request.max_files)
    return response(data=CreateKnowledgeBasesResponse(knowledge_base=KnowledgeBase(id=new_kb.id, name=new_kb.name)))


class SendMessageRequest(BaseModel):
    file_id: Optional[int]
    text: str
    client_ts: int = int(time.time())
    session_id: int
    ref_knowledgebase: bool = True
    ai_msg_signature: str
    user_msg_signature: str


@handle_chat_auth
@handle_request_with_pydantic(SendMessageRequest)
def send_message(request: SendMessageRequest):
    session = data_access.get_session_by_id(request.session_id)
    if not session:
        return response(code=ErrorCodes.session_not_found)

    if session.role not in [ChatRole.assistant, ChatRole.standard_query]:
        return response(code=ErrorCodes.permission_denied)

    chat_context = get_chat_context_history(session, text_only=True)
    chat_summarization = get_summarization_context_history(session, 1)
    summarization = chat_summarization[0] if chat_summarization else None

    user_message, ai_message = data_access.create_message_and_response(
        get_user(), session, request.text, request.client_ts, request.ai_msg_signature, request.user_msg_signature
    )

    default_kb: Optional[models.KnowledgeBaseTab] = data_access.get_user_default_knowledgebase(get_user())
    if request.file_id and (file := data_access.get_file_by_id_user(request.file_id, get_user())):
        task = partial(upload_file_in_chat, user_message, ai_message, file, default_kb)
    elif session.role == ChatRole.assistant:
        task = partial(
            form_record_or_query, request.text, chat_context, user_message, ai_message, summarization)
    elif session.role == ChatRole.standard_query:
        file_ids = [link.file.id for link in default_kb.file_links] if default_kb else []
        ref = retrieve_related_paragraphs(request.text, file_ids)
        task = partial(
            default_rag_chat, request.text, chat_context, list(ref.values()), user_message, ai_message, summarization)
    else:
        task = None
    submit_task(chat_summarization_pool, generate_summarize_task, session=session)
    q = submit_callback_task(task)
    return stream(q)


class RateMessageRequest(BaseModel):
    msg_id: int
    session_id: int
    rating_type: RatingType


@handle_chat_auth
@handle_request_with_pydantic(RateMessageRequest)
def rate_message(request: RateMessageRequest):
    # TODO 点赞时可以把user_message和ai关联起来， 匹配user直接跳表单
    # click like once to light up, click like again to cancel, or click dislike to dislike, dislike it's the same way.
    session = data_access.get_session_by_id(request.session_id)
    if not session:
        return response(code=ErrorCodes.session_not_found)
    message = data_access.get_message_by_msg_id(request.msg_id, session)
    if not message:
        return response(code=ErrorCodes.message_not_found)
    if message.rating == request.rating_type:
        request.rating_type = RatingType.NONE
    data_access.update_message_rating(request.msg_id, request.rating_type, session)
    return response()


# class RetrySendMessageRequest(BaseModel):
#     msg_id: int
#     session_id: int
#
#
# class RetrySendMessageResponse(BaseModel):
#     text: str = ""
#
#
# @handle_chat_auth
# @handle_request_with_pydantic(RetrySendMessageRequest)
# def retry_send_message(request: RetrySendMessageRequest):
#     # 判断是否是最新一条消息，如果是则复用发送消息逻辑(重新调用发消息接口)，重新发送用户消息和ai回答
#     session = data_access.get_session_by_id(request.session_id)
#     if not session:
#         return response(code=ErrorCodes.session_not_found)
#     ai_message = data_access.get_message_by_msg_id(request.msg_id, session)
#     if not ai_message:
#         return response(code=ErrorCodes.message_not_found)
#     if not ai_message.support_retry:
#         return response(code=ErrorCodes.message_not_allow_retry_answer)
#     user_messages = data_access.get_message_by_id(ai_message.question.id)
#     user_card_message = CardMessage.parse_raw(user_messages.content)
#     retry_send_message_response = RetrySendMessageResponse()
#     for component in user_card_message.components:
#         if component.type == CardComponentType.TEXT:
#             retry_send_message_response.text = component.data
#     return response(data=retry_send_message_response)


class SearchKnowledgebaseRequest(BaseModel):
    query: str
    knowledgebase_id: int


@handle_chat_auth
@handle_request_with_pydantic(SearchKnowledgebaseRequest)
def search_knowledgebase(request: SearchKnowledgebaseRequest):
    knowledgebase = data_access.get_knowledge_base_by_id(request.knowledgebase_id)
    if not knowledgebase:
        return response(code=ErrorCodes.knowledge_base_not_found)
    file_ids = [link.file.id for link in knowledgebase.file_links]
    res = retrieve_related_paragraphs(request.query, file_ids)
    return response(data=res)


class FileUploadRequest(BaseModel):
    file_content: str
    filename: str


class FileUploadResponse(BaseModel):
    file_id: int
    filename: str
    file_path: str


@handle_chat_auth
@handle_request_with_pydantic(FileUploadRequest)
def upload_file(request: FileUploadRequest):
    file_content: bytes = base64.b64decode(request.file_content)
    extension = extract_extension(request.filename)
    file_length = len(file_content)
    if file_length <= 0:
        return response(code=ErrorCodes.empty_file)
    if file_length >= runtime_config.max_file_bytes:
        return response(code=ErrorCodes.file_size_exceeded)
    if extension not in runtime_config.supported_file_types:
        return response(code=ErrorCodes.file_extension_invalid)

    content_hash = get_file_hash(file_content)
    file, is_create_file = data_access.upload_file_by_hash(get_user(), content_hash)
    if file:
        return response(data=FileUploadResponse(file_id=file.id, filename=file.name, file_path=file.path))
    oss_file = wrappers.file_system.create_file(file_content, content_hash)
    oss_file.save()
    log.info("upload file, filename=%s, uploaded path=%s", request.filename, oss_file.url)
    file = data_access.create_file(request.filename, extension, oss_file.url, file_length, content_hash, get_user())
    return response(data=FileUploadResponse(file_id=file.id, filename=file.name, file_path=file.path))


class FileUploadByHashRequest(BaseModel):
    file_hash: str


class FileUploadByHashResponse(BaseModel):
    file_id: int
    filename: str
    file_path: str


@handle_chat_auth
@handle_request_with_pydantic(FileUploadByHashRequest)
def upload_file_by_hash(request: FileUploadByHashRequest):
    if file := data_access.get_file_by_hash_user(request.file_hash, get_user()):
        return response(data=FileUploadByHashResponse(file_id=file.id, filename=file.name, file_path=file.path))
    return response(code=ErrorCodes.file_not_found)


class DownLoadFileRequest(BaseModel):
    file_id: int


@handle_chat_auth
@handle_request_with_pydantic(DownLoadFileRequest)
def download_file(request: DownLoadFileRequest):
    file = data_access.get_file_by_id_user(request.file_id, get_user())
    if not file:
        return response(code=ErrorCodes.file_not_found)
    oss_file = wrappers.file_system.create_file(b'', file.content_hash, url=file.path)
    oss_file.load()
    file_content: bytes = oss_file.body
    return file_stream(file_content, file.name)


class GetResourceRequest(BaseModel):
    resource_id: int


class GetResourceResponse(BaseModel):
    # resource: File
    url: str


@handle_chat_auth
@handle_request_with_pydantic(GetResourceRequest)
def get_resource(request: GetResourceRequest):
    file = data_access.get_file_by_id_user(request.resource_id, get_user())
    if not file:
        return response(code=ErrorCodes.file_not_found)
    signed_url = wrappers.lemon.utils.oss_bucket.sign_url(file.path)
    return response(data=GetResourceResponse(url=signed_url))


class ListMessagesRequest(BaseModel):
    session_id: int
    cursor: int
    page_size: int = 20
    action: GetHistoryType = GetHistoryType.BEFORE


class ListMessagesResponse(BaseModel):
    messages: List[Message]
    session_id: int
    cursor: int
    page_size: int = 20
    action: GetHistoryType = GetHistoryType.BEFORE


@handle_chat_auth
@handle_request_with_pydantic(ListMessagesRequest)
def get_history(request: ListMessagesRequest):
    page_size = max(5, min(30, request.page_size))
    session = data_access.get_session_by_id(request.session_id)

    if not session or session.user != get_user():
        log.info("not session or get_history session.user_uuid is different from request.user_id")
        return response(code=ErrorCodes.session_not_found)

    messages = data_access.list_message_by_session_id(session, request.cursor, page_size, request.action)
    return response(data=ListMessagesResponse(
        messages=[Message(**model_to_dict(message),
                          user_msg_id=message.question.msg_id if message.question else None) for message in messages],
        session_id=request.session_id,
        cursor=request.cursor,
        page_size=request.page_size,
        action=request.action
    ))


class UpdateUserInfoRequest(BaseModel):
    avatar: Optional[str]
    nickname: Optional[str]


class UpdateUserInfoResponse(BaseModel):
    avatar: str
    nickname: str
    username: str


@handle_chat_auth
@handle_request_with_pydantic(UpdateUserInfoRequest)
def update_user_info(request: UpdateUserInfoRequest):
    update_num = data_access.update_user_info(request.nickname, request.avatar, get_user())
    if update_num:
        user = models.AuthUserTab.get(id=get_user().id)
        return response(data=UpdateUserInfoResponse(**model_to_dict(user)))
    return response(data=ErrorCodes.database_operation_error)


class ListSearchHistoryRequest(BaseModel):
    version: int


class ListSearchHistoryResponse(BaseModel):
    search_history_list: List[SearchHistory]


@handle_chat_auth
@handle_request_with_pydantic(ListSearchHistoryRequest)
def list_search_history(request: ListSearchHistoryRequest):
    search_history_list = data_access.list_search_history_by_user(get_user(), False)
    return response(data=ListSearchHistoryResponse(search_history_list=[
        SearchHistory(**model_to_dict(search_history)) for search_history in search_history_list]))


class XFAssembleAuthUrlRequest(BaseModel):
    url: str


class XFAssembleAuthUrlResponse(BaseModel):
    final_url: str
    app_id: str


@handle_chat_auth
@handle_request_with_pydantic(XFAssembleAuthUrlRequest)
def assemble_xunfei_auth_url(request: XFAssembleAuthUrlRequest):
    xf_config = data_access.get_xfconfig()
    if not xf_config:
        return response(data=ErrorCodes.xunfei_config_not_found_error)
    xunfei_url = get_xunfei_auth_url(request.url, xf_config.api_secret, xf_config.api_key)

    return response(data=XFAssembleAuthUrlResponse(final_url=xunfei_url, app_id=xf_config.app_id))


class GetReferenceParagraphRequest(BaseModel):
    paragraph_id_list: List[int]


class GetReferenceParagraphResponse(BaseModel):
    paragraphs: List[Paragraph]


@handle_chat_auth
@handle_request_with_pydantic(GetReferenceParagraphRequest)
def get_reference_paragraph(request: GetReferenceParagraphRequest):
    paragraphs: List[Paragraph] = []
    for paragraph_id in request.paragraph_id_list:
        paragraph = data_access.get_paragraph_by_id(paragraph_id)
        if paragraph is None:
            continue
        paragraphs.append(Paragraph(id=paragraph.id, content=paragraph.raw_content))
    return response(data=GetReferenceParagraphResponse(paragraphs=paragraphs))


class ClickButtonEventRequest(BaseModel):
    msg_id: int
    session_id: int
    action: ClickAction


@handle_chat_auth
@handle_request_with_pydantic(ClickButtonEventRequest)
def click_button_event(request: ClickButtonEventRequest):
    session = data_access.get_session_by_id(request.session_id)
    if not session:
        return response(code=ErrorCodes.session_not_found)
    message = data_access.get_message_by_msg_id(request.msg_id, session)
    card = CardMessage.parse_raw(message.content)
    if request.action == ClickAction.after_upload_knowledgebase_file:
        card.remove_all_button()
        if card.components and card.components[0].type == CardComponentType.TEXT:
            card.components.pop(0)
        if card.components and card.components[-1].type != CardComponentType.TEXT:
            card.add_text("你已将文件上传至知识库，可在通知列表查看消息进度")
        data_access.update_message_content_text_context_text(
            request.msg_id, card.json(), "文件已成功上传知识库", "文件已成功上传知识库", session)
    if request.action == ClickAction.after_form_submit:
        card.remove_all_button()
        if card.components and card.components[0].type == CardComponentType.TEXT:
            card.add_text("以上表单已提交成功")
        data_access.update_message_content_text_context_text(
            request.msg_id, card.json(), "以上表单已提交成功", "以上表单已提交成功", session
        )
    new_message = data_access.get_message_by_msg_id(request.msg_id, session)
    # TODO: 更新向量数据库索引
    return response(data=ResponseChunk.base_message(
        request.session_id, request.msg_id, CompleteMessage(**model_to_dict(new_message))))


class SearchMessagesRequest(BaseModel):
    keyword: str
    component_type_list: List[CardComponentType]
    k: int = Field(gt=0, le=20)
    search_ts: int = int(time.time())


class SearchMessagesResponse(BaseModel):
    messages: List[Message]


@handle_chat_auth
@handle_request_with_pydantic(SearchMessagesRequest)
def search_messages(request: SearchMessagesRequest):
    message_pk_list = retrieve_messages(request.keyword, request.component_type_list, get_user(), request.k)
    data_access.create_search_history(request.keyword, request.search_ts, get_user())
    messages = data_access.list_messages_by_id_list(message_pk_list)
    log.info('fetch messages: %s by search result: %s', messages, message_pk_list)

    return response(data=SearchMessagesResponse(
        messages=[Message(**model_to_dict(m)) for m in filter(bool, [messages.get(pk) for pk in message_pk_list])]
    ))


add_route("send_message", send_message)
add_route("rate_message", rate_message)
# add_route("retry_send_message", retry_send_message)
add_route("search_messages", search_messages)

add_route("list_session", list_session)
add_route("get_notification_count", get_notification_count)
add_route("read_notifications", read_notifications)
add_route("list_knowledge_bases", list_knowledge_bases)
add_route("delete_knowledge_bases", delete_knowledge_bases)
add_route("create_knowledge_bases", create_knowledge_bases)
add_route("delete_knowledge_base_file", delete_knowledge_base_file)
add_route("list_knowledge_base_file", list_knowledge_base_file)
add_route("search_knowledgebase", search_knowledgebase)
add_route("file_process_progress", file_process_progress)
add_route("get_reference_paragraph", get_reference_paragraph)

add_route("upload_file", upload_file)
add_route("upload_file_by_hash", upload_file_by_hash)
add_route("upload_knowledge_base_file", upload_knowledge_base_file)
add_route("download_file", download_file)
add_route("get_resource", get_resource)
add_route("get_history", get_history)
add_route("update_user_info", update_user_info)
add_route("click_button_event", click_button_event)

add_route("list_search_history", list_search_history)
add_route("assemble_xunfei_auth_url", assemble_xunfei_auth_url)
