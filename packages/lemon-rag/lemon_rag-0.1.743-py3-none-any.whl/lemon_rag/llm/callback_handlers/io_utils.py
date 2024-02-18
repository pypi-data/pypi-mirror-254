import queue
from typing import Optional

from lemon_rag.utils import log


class StringChannel:
    """for json parse"""

    def __init__(self):
        self.q: queue.Queue = queue.Queue(maxsize=4096)
        self._done: bool = False
        self.exception: Optional[Exception] = None
        self.start = False
        self.end = False

    def _read(self, size: int = 1024, *args, **kwargs):
        if size == 0:
            return ""
        if self._done and self.q.empty():
            return ""
        if self.exception:
            return ""
        try:
            return self.q.get(timeout=15)
        except queue.Empty:
            return ""

    def read(self, size: int = 1024, *args, **kwargs):
        data = self._read(size, *args, **kwargs)
        return data

    def write(self, data: str):
        for d in data:
            if d == "{":
                self.start = True
            if d == "}":
                self.end = True
                self._done = True
                self.q.put(d)
            if self.start and not self.end:
                self.q.put(d)

    def done(self):
        self._done = True

    def read_all(self) -> str:
        res = []
        while not self.q.empty():
            res.append(self.read())
        return "".join(res)

    def close(self):
        self._done = True

    def error(self, error: Exception):
        log.info("StringChannel got and error: %s", error)
        self.exception = error
