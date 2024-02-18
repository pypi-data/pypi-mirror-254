import hashlib


def get_file_hash(file_content: bytes) -> str:
    return hashlib.sha256(file_content).hexdigest()
