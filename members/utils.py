import time
import hashlib


def md5_hash(message):
    if message is None:
        raise ValueError("Can't hash a None value.")
    return hashlib.md5(message.encode("utf-8")).hexdigest()


def verify_link(email, secret, timestamp, token):
    email = email.strip()
    if not bool(email):
        return False

    token = token.strip()
    if not bool(token):
        return False

    message = "".join([email, secret, str(timestamp)])
    hash_value = md5_hash(message)
    return (int(time.time()) <= int(timestamp) and hash_value == token)
