import queue
from abc import ABC, abstractmethod

from pydantic import BaseModel

from lemon_rag.lemon_runtime import models
from lemon_rag.protocols.chat import CardMessage


class ToolFunction(BaseModel, ABC):

    @abstractmethod
    def execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        pass
