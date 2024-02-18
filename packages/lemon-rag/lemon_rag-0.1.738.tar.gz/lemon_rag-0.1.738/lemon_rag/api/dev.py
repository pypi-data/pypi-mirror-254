import base64
import os
import subprocess
import tempfile

from pydantic import BaseModel

from lemon_rag.api.base import handle_request_with_pydantic, add_route, handle_chat_auth
from lemon_rag.utils.response_utils import response


class UpgradeRequest(BaseModel):
    package_content: str
    filename: str


@handle_request_with_pydantic(UpgradeRequest)
def handle_upgrade(req: UpgradeRequest):
    with tempfile.TemporaryDirectory() as tmpdirname:
        whl_path = os.path.join(tmpdirname, req.filename)
        with open(whl_path, "wb") as f:
            f.write(base64.b64decode(req.package_content))
        output = subprocess.check_output(
            ['pip', 'install', whl_path],
            stderr=subprocess.STDOUT, universal_newlines=True
        )
    return response(data=output)


