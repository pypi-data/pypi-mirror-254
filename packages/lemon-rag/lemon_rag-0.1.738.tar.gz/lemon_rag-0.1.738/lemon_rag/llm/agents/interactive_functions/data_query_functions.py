import queue
from typing import Union

from langchain_core.messages import get_buffer_string

from lemon_rag.dependencies.data_access import data_access
from lemon_rag.lemon_runtime import models
from lemon_rag.llm.agents.interactive_functions.base_function import ToolFunction
from lemon_rag.llm.agents.prompts.select_query_command import select_query_function
from lemon_rag.llm.callback_handlers.text_callback_handler import TextCallbackHandler
from lemon_rag.protocols.chat import CardMessage
from lemon_rag.protocols.query_methods import query_functions
from lemon_rag.utils import log
from lemon_rag.utils.api_utils import get_chat_context_history, get_send_text_message_function


class QueryOrAnalysisData(ToolFunction):
    """query, search or analysis employee info, project info, transaction details, salary bills, receivable/payable bills etc."""
    requirement: str

    def execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        session = data_access.get_session_by_id(ai_message.session.id)
        chat_context = get_chat_context_history(session, text_only=True)
        log.info('[QueryOrAnalysisData] ChatContext=%s', get_buffer_string(chat_context))
        session_id = ai_message.session.id
        msg_id = ai_message.msg_id
        send_text_message_func = get_send_text_message_function(q, session_id, msg_id, card)
        res: Union[str, ToolFunction] = select_query_function(
            chat_context, query_functions=query_functions, callbacks=[TextCallbackHandler(send_text_message_func)]
        )
        if isinstance(res, str):
            return ""

        return res.execute(q, ai_message, user_requirement, card)
