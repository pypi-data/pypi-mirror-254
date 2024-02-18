import asyncio
import queue
from queue import Queue
from typing import TypeVar, Any

import sanic.response
import sanic.response as sanic_response
from pydantic import BaseModel

from lemon_rag.utils import log

T = TypeVar("T")

timeout = 120


class ErrorCode(BaseModel):
    status: int = 200
    code: int
    message: str


class ErrorCodes:
    ok = ErrorCode(code=20000, message="OK")
    invalid_json = ErrorCode(code=40001, message="请求JSON格式错误")
    username_existed = ErrorCode(code=40002, message="用户名已存在")
    invalid_username_or_password = ErrorCode(code=40003, message="用户名或密码不正确")
    invalid_file_format = ErrorCode(code=40004, message="暂不支持该文件类型")
    pdf_invalid = ErrorCode(code=40005, message="PDF为扫描件或内容为空")
    unauthorized = ErrorCode(code=40100, message="未登录", status=401)
    invalid_token = ErrorCode(code=40101, message="无效的令牌", status=401)
    file_size_exceeded = ErrorCode(code=40102, message="文件尺寸超出限制，请将文件尺寸控制在3MB以内")
    empty_file = ErrorCode(code=40103, message="上传的文件为空，请检查后重新上传")
    file_count_exceeded = ErrorCode(code=40104, message="上传文件数量超过限制，每个知识库最多上传5个文件")
    file_extension_invalid = ErrorCode(code=40105, message="暂不支持该文件类型")
    database_operation_error = ErrorCode(code=40106, message="数据库操作异常")
    knowledge_base_existed = ErrorCode(code=40107, message="知识库名称已存在")
    xunfei_config_not_found_error = ErrorCode(code=40108, message="找不到讯飞配置，请在web端管理页面添加配置")

    quick_create_invalid = ErrorCode(code=40109, message="暂不支持快速创建该数据")

    permission_denied = ErrorCode(code=40300, message="你没有权限执行此操作")
    internal_server_error = ErrorCode(code=50000, message="服务器内部错误", status=500)
    knowledge_base_not_found = ErrorCode(code=40400, message="知识库不存在")
    file_not_found = ErrorCode(code=40401, message="文件不存在")
    session_not_found = ErrorCode(code=40402, message="会话不存在")
    message_not_found = ErrorCode(code=40403, message="消息不存在")
    message_not_allow_retry_answer = ErrorCode(code=40404, message="消息不允许重新回答")


class Response(BaseModel):
    code: int
    message: str = ""
    data: Any


def response(code: ErrorCode = ErrorCodes.ok, data: T = ""):
    if isinstance(data, BaseModel):
        data = data.dict()
    return sanic_response.json(
        Response(**{"code": code.code, "data": data, "message": code.message}).dict(),
        status=code.status
    )


def file_stream(content: bytes, filename: str):
    headers = {
        'Content-Type': 'application/octet-stream',
        "Content-Disposition": f"attachment; filename={filename}"
    }
    return sanic_response.HTTPResponse(body_bytes=content, headers=headers)


def stream(q: Queue):
    async def stream_from_queue(res: sanic_response.StreamingHTTPResponse):
        total_sleep = 0
        while True:
            if total_sleep >= timeout:
                raise TimeoutError()
            try:
                log.info("try to read the q")
                data = q.get_nowait()
                log.info("read q data: %s", data)
                if data == "end":
                    break
                await res.write(data+"\n")
                log.info("written q data: %s", data)
            except queue.Empty:
                log.info("read q empty, sleep 0.5s")
                await asyncio.sleep(0.5)
                total_sleep += 0.5
                log.info("sleep end")
            except Exception as e:
                log.info("An exception occurred: %s", str(e))
                raise

    return sanic_response.stream(stream_from_queue)
