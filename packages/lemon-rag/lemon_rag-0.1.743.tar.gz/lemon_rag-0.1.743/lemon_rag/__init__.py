from lemon_rag.api.auth import hello_world, hello_stream, register
from lemon_rag.api.base import handle_all_api
from lemon_rag.patch.patch_vars import patch_all
import lemon_rag.api.chat
import lemon_rag.api.business
import lemon_rag.api.dev
from lemon_rag.scheduler.base_scheduler import check_and_do_schedule

debug_exec = exec
