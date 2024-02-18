from typing import List, Optional

from langchain_core.messages import HumanMessage, BaseMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate

from lemon_rag.dependencies.data_access import data_access
from lemon_rag.lemon_runtime import models
from lemon_rag.llm.client.base_client import ChatChain, get_llm
from lemon_rag.utils import log
from lemon_rag.utils.api_utils import get_chat_context_history, get_summarization_context_history

system_message_template = """
## Role
You are a chat summarizing assistant. Your duty is helping the user to summarize the chat histories.
Here are the chat history between the AI and the Human. You need to analyse their conversation and summarize it briefly. 
Your summarization will be used as the context of the latter conversation. {placeholder}
"""


def generate_summarize(histories: List[BaseMessage], summarization: Optional[BaseMessage] = None):
    chat_chain = ChatChain(
        llm=get_llm(max_tokens=300),
        template=(ChatPromptTemplate.from_strings(
            [(SystemMessagePromptTemplate, system_message_template)]) + ([SystemMessage(content=summarization.content)] if summarization else []) + histories + [HumanMessage(content="Please output a summarization based on the above chat records without any other explanation.")]
    ))

    # log.info(chat_chain.template.format(placeholder=""))

    result = chat_chain.run(placeholder="")
    return result


def generate_summarize_task(session: models.SessionTab):
    message_count = data_access.get_message_count(session)

    log.info(f"===============消息数 {message_count}")

    # message's summarization
    if message_count > 0 and message_count % 10 == 0:
        histories = get_chat_context_history(session)
        chat_summarization = get_summarization_context_history(session, 1)
        summarization = chat_summarization[0] if chat_summarization else None

        result = generate_summarize(histories, summarization)
        history_messages = data_access.get_last_message_by_session_id(session)
        first_message, last_message = history_messages[0], history_messages[-1]

        data_access.create_message_summarization(
            first_message.msg_id, last_message.msg_id, result, len(history_messages), session)
