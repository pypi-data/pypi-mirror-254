import threading

from lemon_rag.scheduler.vectorize_sentences import vectorize_sentences
from lemon_rag.utils import log

lock = threading.Lock()


def check_and_do_schedule():
    if lock.locked():
        log.info("another thread is already running")
        return
    with lock:
        vectorize_sentences()

    log.info("scheduler done")
