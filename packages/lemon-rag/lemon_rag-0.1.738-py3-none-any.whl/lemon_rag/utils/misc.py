import base64
import random
import string


def generate_random_username() -> str:
    prefix = "用户"
    random_bytes = random.choices(string.ascii_letters.encode(), k=6)
    base64_string = base64.b64encode(bytes(random_bytes)).decode()[:8]
    username = prefix + base64_string
    return username


