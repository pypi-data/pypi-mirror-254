import datetime
import queue
from typing import List, Optional

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate

from lemon_rag.dependencies.data_access import data_access
from lemon_rag.lemon_runtime import models
from lemon_rag.llm.agents.interactive_functions.base_function import ToolFunction
from lemon_rag.llm.agents.rag.vectorization.runner import vectorization_pool, vectorize_message
from lemon_rag.llm.callback_handlers.text_callback_handler import TextCallbackHandler
from lemon_rag.llm.client.base_client import ChatChain
from lemon_rag.protocols.chat import RefFileWithContent, ResponseChunk, CardMessage
from lemon_rag.utils import log
from lemon_rag.utils.api_utils import send_base_message, get_send_text_message_function
from lemon_rag.utils.executor_utils import submit_task

system_message_template = """
# Role
You are an AI personal assistant. 
Your responsibility is to answer user's questions based on the reference files or chat to user.

# Restrictions
* If the reference data contains any information useful, you are preferred to quote the referred paragraphs.

Here are some reference data:
{reference_paragraphs}

Now it is {datetime}, Now please start to assistant the user in chinese.
"""


def assemble_reference_paragraphs(reference_paragraphs: List[RefFileWithContent]) -> str:
    lines = []
    for ref in reference_paragraphs:
        lines.append(f"# {ref.origin_filename}")
        for c in ref.content:
            lines.append(c)
    return "\n".join(lines)


def default_rag_chat(
        user_input: str,
        histories: List[BaseMessage],
        reference_paragraphs: List[RefFileWithContent],
        user_message: Optional[models.MessageTab],
        ai_message: Optional[models.MessageTab],
        summarization: Optional[BaseMessage],
        q: queue.Queue
) -> str:
    log.info("executing default_rag_chat, user_input=%s", user_input)
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

    chat_chain = ChatChain(template=ChatPromptTemplate.from_strings([
            (SystemMessagePromptTemplate, system_message_template)
        ] + ([SystemMessage(content=f"History Summarization: {summarization.content}")] if summarization else [])
        + histories + [HumanMessage(content=user_input)]
    ))

    # log.info(chat_chain.template.format(**{
    #     "reference_paragraphs": assemble_reference_paragraphs(reference_paragraphs),
    #     "datetime": datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    # }))

    result = chat_chain.run(
        callbacks=callbacks,
        reference_paragraphs=assemble_reference_paragraphs(reference_paragraphs),
        datetime=datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    )

    log.info(
        f"ai generate: {result}, 类型：{type(result)}, 属于tool_function类型: {isinstance(result, ToolFunction)}")
    if reference_paragraphs:
        q.put(ResponseChunk.add_ref_file(session_id, msg_id, reference_paragraphs, card).json())
    # 将消息组件作为倒排索引录入向量数据库
    submit_task(vectorization_pool, vectorize_message, user_message, CardMessage.parse_raw(user_message.content))
    submit_task(vectorization_pool, vectorize_message, ai_message, card)
    data_access.update_message_content_text_context_text(msg_id, card.json(), result, result, ai_message.session)
    return result


if __name__ == '__main__':
    q = queue.Queue(maxsize=1000)
    default_rag_chat(
        "你好，请问夏朝是什么时候",
        [],
        [],
        None,
        None,
        q
    )
