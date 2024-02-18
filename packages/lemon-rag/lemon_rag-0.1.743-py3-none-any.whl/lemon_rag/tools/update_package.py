import base64
import os.path
import subprocess
import sys
import time

import requests
from requests import HTTPError

from lemon_rag.configs.local_dev_config import config


def wait_for_pypi_index(package: str, v: str):
    while True:
        try:
            r = requests.get(f"https://pypi.org/project/{package}/{v}/")
            r.raise_for_status()
            print("index finished")
            return
        except Exception as e:
            print("still indexing", e)
            time.sleep(1)


def api_update_current_package(package: str, v: str):
    wait_for_pypi_index(package, v)
    url = f"https://lemon.lemonstudio.tech:8443/{config.lemon_rag.app_uuid}test/{config.lemon_rag.tenant_uuid}/restful/v1/update_module"
    print(url)
    res = requests.post(
        url,
        json={"name": package, "version": v, "registry": "https://pypi.python.org/simple/"}

    )
    res.raise_for_status()
    print(res.json().get("output"))


def hello():
    url = f"https://lemon.lemonstudio.tech:8443/{config.lemon_rag.app_uuid}test/{config.lemon_rag.tenant_uuid}/restful/v1/hello_world"
    res = requests.get(url)
    res.raise_for_status()


def restart_server():
    print("try to send the restart signal")
    url = f"https://lemon.lemonstudio.tech:8443/{config.lemon_rag.app_uuid}test/{config.lemon_rag.tenant_uuid}/restful/v1/restart_server"
    requests.get(url)
    print("sent restart signal to the server")

    while True:
        try:
            hello()
            return
        except HTTPError as e:
            print(f"[{e.response.status_code}] server starting......")
            time.sleep(1)


def install_directly(package: str, v: str):
    url = f"https://lemon.lemonstudio.tech:8443/{config.lemon_rag.app_uuid}test/{config.lemon_rag.tenant_uuid}/restful/v1/direct_upgrade_package"
    print(url)
    filename = f"lemon_rag-{v}-py3-none-any.whl"
    res = requests.post(
        url,
        json={"package_content": base64.b64encode(open(os.path.join("dist", filename), "rb").read()).decode(),
              "filename": filename}
    )
    res.raise_for_status()
    print(res.json().get("data"))


if __name__ == '__main__':
    if len(sys.argv[1:]) == 2:
        name, version = sys.argv[1:]
    else:
        poetry_version_output = subprocess.run(["poetry", "version"], capture_output=True, text=True)
        name, version = poetry_version_output.stdout.strip().split(' ')
    while True:
        try:
            install_directly(name, version)
            break
        except Exception as e:
            print(e, "server install new package failed")
            time.sleep(1)

    restart_server()
