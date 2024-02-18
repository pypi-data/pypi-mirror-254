import importlib

import peewee
from sanic import response

from lemon_rag.patch.patch_nginx import patch_and_restart_nginx


def patch_models(lemon):
    from lemon_rag.lemon_runtime import models
    for attr_name in dir(models):

        attr = getattr(models, attr_name)
        # print(type(attr))
        if not isinstance(attr, type):
            continue
        if not issubclass(attr, peewee.Model):
            continue
        runtime_model = lemon.lemon_rag.get(attr_name, lemon.project_ledger.get(attr_name))
        setattr(models, attr_name, runtime_model)


def patch_log(lemon):
    from lemon_rag.utils import log
    setattr(log, "lemon_info", lemon.utils.log.info)


def patch_wrappers(lemon):
    from lemon_rag.lemon_runtime import wrappers
    setattr(wrappers, "file_system", lemon.filesystem)
    setattr(wrappers, "lemon", lemon)


def patch_codes(lemon):
    class Response:
        HTTPResponse = (response.HTTPResponse, response.StreamingHTTPResponse)

    restful = importlib.import_module("runtime.component.restful")
    setattr(restful, "response", Response())


def patch_all(lemon):
    patch_models(lemon)
    patch_log(lemon)
    patch_wrappers(lemon)
    patch_codes(lemon)
    patch_and_restart_nginx()
