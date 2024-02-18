import copy
import importlib
import traceback
from _weakrefset import WeakSet
from concurrent.futures import ThreadPoolExecutor, Executor
from typing import Callable

from lemon_rag.api.local import get_user, get_rid, with_rid, with_auth
from lemon_rag.utils import log


def submit_task(executor: Executor, func: Callable, *args, **kwargs):
    utils = None
    try:
        utils = importlib.import_module("baseutils.utils")
        cu = utils.LemonContextVar.current_user.get()
        copy_cu = copy.copy(cu)
    except:
        pass

    user = get_user()
    rid = get_rid()

    def inner(*args, **kwargs):
        with with_rid(rid):
            with with_auth(user):
                if utils:
                    utils.LemonContextVar.current_user.set(copy_cu)
                    utils.LemonContextVar.current_connector.set(None)
                    utils.LemonContextVar.other_connector.set(None)
                    utils.LemonContextVar.current_root_form.set(None)
                    utils.LemonContextVar.current_transaction.set(None)
                    utils.LemonContextVar.current_lsm.set(None)
                    utils.LemonContextVar.current_workspace.set(None)
                    utils.LemonContextVar.taskid.set(None)
                    utils.LemonContextVar.condition.set(None)
                    utils.LemonContextVar.atomic_resource_locks.set(None)
                    utils.LemonContextVar.atomic_instances.set(WeakSet())
                    log.info("background task, current_user: %s", copy_cu.tenant_uuid)
                try:
                    return func(*args, **kwargs)
                except:
                    log.info("dispatch background task failed, %s", traceback.format_exc())

    return executor.submit(inner, *args, **kwargs)
