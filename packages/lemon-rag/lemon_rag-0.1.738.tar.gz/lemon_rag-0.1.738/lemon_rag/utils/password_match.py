import hashlib


def hash_password(password: str) -> str:
    # Hash the password using SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    return hashed_password
