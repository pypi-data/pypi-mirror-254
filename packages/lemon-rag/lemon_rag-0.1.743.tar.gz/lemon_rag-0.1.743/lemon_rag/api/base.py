import importlib
import traceback
from datetime import datetime
from typing import Callable, Union, Type, Dict, Optional

import sanic.request
from pydantic import BaseModel, ValidationError
from sanic import response

from lemon_rag.api.local import with_auth, with_rid
from lemon_rag.lemon_runtime import models
from lemon_rag.settings import LemonEnv, lemon_env
from lemon_rag.utils import response_utils, log
from lemon_rag.utils.response_utils import ErrorCodes
from lemon_rag.dependencies.data_access import data_access

PydanticRequestHandler_F = Callable[[BaseModel], response.HTTPResponse]
Handler_F = Callable[[sanic.request.Request], Union[response.HTTPResponse, response.StreamingHTTPResponse]]
Response_T = Union[response.HTTPResponse, response.StreamingHTTPResponse]
TOKEN_KEY = "Authorization"


def extract_token(req: sanic.request.Request) -> str:
    token = req.headers.get(TOKEN_KEY, "")
    if token.startswith("Bearer "):
        return token[7:]
    return token


def handle_chat_auth(func: Handler_F) -> Handler_F:
    def inner(request: sanic.request.Request) -> Response_T:
        token = extract_token(request)
        if not token:
            log.info("Token not found, request_header=%s", request.headers)
            return response_utils.response(code=ErrorCodes.unauthorized)
        data_access.delete_expired_token()
        token_record: Optional[models.AppAuthTokenTab] = models.AppAuthTokenTab.get_or_none(token=token)
        if not token_record:
            log.info("Token invalid, token_record=%s", token_record)
            return response_utils.response(code=ErrorCodes.invalid_token)

        auth_user = token_record.user
        if not auth_user:
            log.info("user not found, token_record=%s", token_record)
            return response_utils.response(code=ErrorCodes.invalid_token)

        with with_auth(auth_user):
            res = func(request)
        return res

    return inner


def handle_request_with_pydantic(request_type: Type[BaseModel]) -> Callable[[PydanticRequestHandler_F], Handler_F]:
    def decorator(func: PydanticRequestHandler_F) -> Handler_F:
        def inner(request: sanic.request.Request, *args, **kwargs) -> Response_T:
            try:
                structured_req = request_type.parse_obj(request.json)
            except ValidationError as e:
                return response_utils.response(
                    code=ErrorCodes.invalid_json, data={"errors": e.errors()}
                )
            res = func(structured_req)
            return res

        return inner

    return decorator


ai_assistant_api_mapping: Dict[str, Handler_F] = {}


def add_route(path, handler: Handler_F):
    ai_assistant_api_mapping[path] = handler


class DisableTransaction:
    def __init__(self):
        self.utils = importlib.import_module("baseutils.utils")
        self.transaction = self.utils.LemonContextVar.current_transaction.get()

    def __enter__(self):
        self.utils.LemonContextVar.current_transaction.set(None)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.utils.LemonContextVar.current_transaction.set(self.transaction)


def handle_all_api(request: sanic.request.Request, sub_path: str) -> Response_T:
    with with_rid() as rid:
        try:
            # disable the transaction
            with DisableTransaction():
                handler = ai_assistant_api_mapping.get(sub_path)
                if not handler:
                    log.info("handler not found, path=%s, available paths=%s", sub_path,
                             list(ai_assistant_api_mapping.keys()))
                    return response.text(f"Not Found\nrid:{rid}", status=404)
                res = handler(request)
                res.headers.setdefault("rid", rid)
                return res
        except Exception as e:
            log.info("[handle_all_api] error occurred] %s %s", e, traceback.format_exc().replace("\n", "||"))
            if lemon_env == LemonEnv.live:
                return response_utils.response(code=ErrorCodes.internal_server_error)
            return response.text(f"{e}\n{traceback.format_exc()}", status=500)
