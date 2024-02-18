import requests

from lemon_rag.configs.local_dev_config import config

def run():
    code = open("debug.py", "r", encoding="utf-8").read()
    res = requests.post(
        f"https://lemon.lemonstudio.tech:8443/{config.lemon_rag.app_uuid}test/{config.lemon_rag.tenant_uuid}/restful/v1/debug_code",
        json={"code": code}
    )
    res.raise_for_status()

    print("\n".join(res.json().get("output")))

if __name__ == '__main__':
    run()