import os
from enum import Enum

LEMON_MODULE_NAME = "AI助手"

lemon_env = os.environ.get("LEMON_ENV", "Development")


class LemonEnv(str, Enum):
    dev = "Development"
    test = "Testing"
    live = "Production"
