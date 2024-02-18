import copy
import importlib
import queue
import traceback
from concurrent.futures import ThreadPoolExecutor
from typing import Generator, Iterable, Callable, Optional

from lemon_rag.utils import log
from lemon_rag.utils.executor_utils import submit_task

streaming_pool = ThreadPoolExecutor(max_workers=16)


def submit_generator_task(generator: Iterable[str]) -> queue.Queue:
    q = queue.Queue(maxsize=128)

    def inner_task():
        for value in generator:
            print("iterate the generator", value)
            q.put(value)
        q.put("end")

    streaming_pool.submit(inner_task)
    return q


CallbackTask = Callable[[queue.Queue], None]


def submit_callback_task(t: Optional[CallbackTask]) -> queue.Queue:
    q = queue.Queue(maxsize=1024)

    def inner():
        try:
            if t:
                t(q)
        except Exception as e:
            log.info("Stream Response Exception, %s", traceback.format_exc())
        finally:
            q.put("end")
    submit_task(streaming_pool, inner)
    return q
