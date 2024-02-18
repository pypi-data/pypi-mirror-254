import time
import uuid
from asyncio import Queue
from typing import Optional

import sanic.request
from playhouse.shortcuts import model_to_dict
from pydantic import BaseModel

from lemon_rag.api.base import handle_request_with_pydantic, add_route, handle_chat_auth
from lemon_rag.api.local import get_user
from lemon_rag.core.executor_pool import submit_callback_task
from lemon_rag.dependencies.data_access import data_access
from lemon_rag.lemon_runtime import models
from lemon_rag.utils import log
from lemon_rag.utils.init_utils import init_transaction_item
from lemon_rag.utils.misc import generate_random_username
from lemon_rag.utils.password_match import hash_password
from lemon_rag.utils.response_utils import response, stream, ErrorCodes


def hello_world(request: sanic.request.Request):
    return response()


def hello_stream(request: sanic.request.Request):
    def generator(q: Queue):
        for line in ["aaaaa", "bbbbb", "ccccc", "ddddd"]:
            q.put(line)
            time.sleep(1)

    queue = submit_callback_task(generator)

    return stream(queue)


class RegisterRequest(BaseModel):
    username: str
    password: str


class RegisterResponse(BaseModel):
    id: int
    username: str
    nickname: str
    last_signin: str
    avatar: str


@handle_request_with_pydantic(RegisterRequest)
def register(req: RegisterRequest):
    existed_user: Optional[models.AuthUserTab] = models.AuthUserTab.get_or_none(username=req.username)
    if existed_user:
        log.info("[register] existed user, username=%s", req.username)
        return response(code=ErrorCodes.username_existed)

    user = models.AuthUserTab.create(**{
        "username": req.username,
        "password": hash_password(req.password),
        "nickname": generate_random_username(),
        "mobile_number": "",
        "avatar": ""
    })
    data_access.init_account(user)
    init_transaction_item(user)

    return response(data=RegisterResponse(**model_to_dict(user)))


class SignInRequest(BaseModel):
    username: str
    password: str


class SignInResponse(BaseModel):
    id: int
    token: str
    avatar: str
    nickname: str
    username: str


@handle_request_with_pydantic(SignInRequest)
def sign_in(req: RegisterRequest):
    auth_user = models.AuthUserTab.get_or_none(username=req.username)
    if not auth_user:
        return response(code=ErrorCodes.invalid_username_or_password)

    if auth_user.password != hash_password(req.password):
        return response(code=ErrorCodes.invalid_username_or_password)

    token = data_access.generate_new_auth_token(auth_user)
    return response(data=SignInResponse(token=token.token, **model_to_dict(auth_user)))


class SignOutRequest(BaseModel):
    token: str


@handle_chat_auth
@handle_request_with_pydantic(SignOutRequest)
def sign_out(req: SignOutRequest):
    delete_num = data_access.delete_token_by_user(req.token, get_user())
    if delete_num:
        return response()
    return response(data=ErrorCodes.database_operation_error)


add_route("register", register)
add_route("sign_in", sign_in)
add_route("sign_out", sign_out)
