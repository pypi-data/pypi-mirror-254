import threading
import uuid
from contextlib import contextmanager
from typing import Optional

from lemon_rag.lemon_runtime.wrappers import RuntimeFile

request_context = threading.local()


def get_rid() -> str:
    if hasattr(request_context, "rid"):
        return request_context.rid
    return "not-set"


def get_user():
    if hasattr(request_context, "user"):
        return request_context.user
    return None


@contextmanager
def with_rid(rid: str = ""):
    try:
        if not rid:
            rid = uuid.uuid4().hex
        request_context.rid = rid
        yield rid
    finally:
        del request_context.rid


@contextmanager
def with_auth(auth_user):
    try:
        request_context.user = auth_user
        yield
    finally:
        del request_context.user
