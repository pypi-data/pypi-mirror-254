import traceback

from lemon_rag.api.local import get_rid, get_user
from lemon_rag.settings import lemon_env


def lemon_info(value: str):
    pass


file = "/var/log/supervisor/backup.log" if lemon_env != "Development" else "backup.log"


def info(msg: str, *args):
    suffix = f" rid={get_rid()} user_id={get_user()}"
    try:
        log_expr = (msg + suffix) % args
        print(log_expr)
        lemon_info(log_expr)
        with open(file, "a") as f:
            f.write(log_expr + "\n")
    except Exception as e:
        error_msg = f"[[{msg}]]" + "\n" + traceback.format_exc()
        print(error_msg)
        lemon_info(error_msg)
        with open(file, "a") as f:
            f.write(error_msg + "\n")
