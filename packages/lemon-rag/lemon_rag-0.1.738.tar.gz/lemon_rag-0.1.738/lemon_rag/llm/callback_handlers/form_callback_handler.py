import queue
from typing import Any, Union, Dict, List, Optional, Generator, Callable
from uuid import UUID

import ijson
from langchain.schema import LLMResult
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import GenerationChunk, ChatGenerationChunk

from lemon_rag.lemon_runtime import models
from lemon_rag.llm.callback_handlers.io_utils import StringChannel
from lemon_rag.protocols.chat import FormSchema, CardMessage, ResponseChunk, FormComponent, FormData
from lemon_rag.utils import log


class StringChannelCallbackHandler(BaseCallbackHandler):

    def __init__(self, c: StringChannel):
        self.c = c

    @property
    def always_verbose(self) -> bool:
        """Whether to call verbose callbacks even if verbose is False."""
        return True

    def on_llm_start(
            self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when LLM starts running."""

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        if token:
            self.c.write(token)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        self.c.close()

    def on_llm_error(
            self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        self.c.error(error)


class JSONLineCallbackHandler(BaseCallbackHandler):
    run_inline = True

    def __init__(self, q: queue.Queue):
        self.value: str = ""
        self.q = q
        self.current_channel: Optional[StringChannel] = None

    def on_llm_end(
            self,
            response: LLMResult,
            *,
            run_id: UUID,
            parent_run_id: Optional[UUID] = None,
            **kwargs: Any,
    ) -> Any:
        self.q.put("")
        self.current_channel and self.current_channel.done()

    def on_llm_error(
            self,
            error: BaseException,
            *,
            run_id: UUID,
            parent_run_id: Optional[UUID] = None,
            **kwargs: Any,
    ) -> Any:
        self.q.put("")
        self.current_channel and self.current_channel.done()

    def on_llm_new_token(
            self,
            token: str,
            *args,
            **kwargs: Any,
    ) -> Any:
        for char in token:
            self.value += char
            if ("\n" in self.value) or (self.current_channel is None):
                self.value = self.value.split("\n")[-1]
                if self.current_channel:
                    self.current_channel.done()
                    self.current_channel = None
                if not self.value.startswith("{"):
                    continue
                self.current_channel = StringChannel()
                self.current_channel.write(self.value)
                self.q.put(self.current_channel)
                log.info("find json line, send the string channel")
                continue

            if self.current_channel:
                self.current_channel.write(char)


if __name__ == '__main__':
    q = queue.Queue(maxsize=10)
    input_text = """{"date": "2024-01-17", "project": "冰雪大世界", "voucher_number": "", "type": "支出", "payment_account": "", "purpose": "建材", "transaction_summary": "购买40袋水泥", "amount": "3000", "customer": "", "supplier": "宁波水泥厂"}
{"date": "2024-01-17", "project": "广州琶洲蜜雪冰城", "voucher_number": "", "type": "支出", "payment_account": "", "purpose": "建材", "transaction_summary": "购买60块玻璃", "amount": "100000", "customer": "", "supplier": "广州有爱玻璃厂"}
"""
    ch = JSONLineCallbackHandler(q)
    for char in input_text:
        ch.on_llm_new_token(char)
    while not q.empty():
        channel: StringChannel = q.get()
        for key, value in ijson.kvitems(channel, ""):
            print(key, value)
