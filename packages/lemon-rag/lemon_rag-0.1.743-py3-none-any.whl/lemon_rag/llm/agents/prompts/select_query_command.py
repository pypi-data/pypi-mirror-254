import datetime
from typing import List, Union, Type

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import BaseMessage, HumanMessage, get_buffer_string
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate

from lemon_rag.llm.agents.interactive_functions.base_function import ToolFunction
from lemon_rag.llm.client.base_client import ChatChain

system_message_template = """
# Role
You are a assistant. Your duty is help the user to management his project data.
You will be given some requirement from the user, 
you need to analyse the user's requirement and select the proper function call to satisfy the user's requirement.

# Restrictions
* You can just leave the unused parameters empty.
* If the user didn't provide enough information, you can call the command RaiseError.
* date format should be %Y年%M月%D日, date range should be two date split by~
* Use the Chinese as the default langauge.
* You can ask the user for the necessary information.

# Context
It is {date} now.
Chat histories between you and the user:
{chat_histories}
# Output Example
Human Input:
帮我查一下xxx项目上周的支出情况
AI:
call `QueryTransactions`

Human Input:
帮我看一下xx项目还有多少钱没有收回来
AI:
call `QueryPayableOrReceivableBills`

please start to assistant the user based on the instructions above.
"""


def select_query_function(
        chat_histories: List[BaseMessage], query_functions: List[Type[ToolFunction]],
        callbacks: List[BaseCallbackHandler]
) -> Union[str, ToolFunction]:
    chain = ChatChain(template=ChatPromptTemplate.from_strings(
        [
            (SystemMessagePromptTemplate, system_message_template)
        ] + chat_histories),
        functions=query_functions
    )
    date = datetime.datetime.now().strftime("%Y年%m月%d日")
    res = chain.run(
        date=date, chat_histories=get_buffer_string(chat_histories), callbacks=callbacks
    )
    return res
