import inspect
import types
import uuid
from typing import List

import sanic.request

import lemon_rag
from lemon_rag.configs.local_dev_config import config
from lemon_rag.tools.sync_datamodel import DesignClient, Document

function_list = []
for attr_name in dir(lemon_rag):
    attr = getattr(lemon_rag, attr_name)
    if not isinstance(attr, types.FunctionType):
        continue

    sig = inspect.signature(attr)
    if sig.parameters and list(sig.parameters.values())[0].annotation == sanic.request.Request:
        function_list.append(attr_name)

client = DesignClient(**config.lemon_rag.dict())
documents: List[Document] = client.list_document("15d8cb84699a599585be2988076bb90e")
existed_document_set = {d.document_name for d in documents}


def lemon_uuid():
    return str(uuid.uuid5(uuid.uuid1(), str(uuid.uuid1()))).replace("-", "")


for api in function_list:
    if api not in existed_document_set:
        print(f"{api} is not synced, start syncing")
    client.create_cloud_func(
        api, {
            "func": f"lemon_rag = lemon.lemon_rag.load_module(\"lemon_rag\")\nreturn lemon_rag.{api}(request)",
            "icon": "",
            "name": api,
            "uuid": lemon_uuid(),
            "arg_list": [
                {
                    "name": "request",
                    "description": ""
                }
            ],
            "description": "",
            "return_list": [
                {
                    "name": "response",
                    "description": ""
                }
            ],
            "install_sm_toolbox": False
        }, "15d8cb84699a599585be2988076bb90e"
    )
