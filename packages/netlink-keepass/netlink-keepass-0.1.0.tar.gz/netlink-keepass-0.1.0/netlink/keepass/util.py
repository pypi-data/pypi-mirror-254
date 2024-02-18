import base64
from collections import namedtuple

from cryptography.fernet import Fernet

FernetToken = namedtuple('FernetToken', ['token', 'key'])


def fernet_token(secret: str):
    key = Fernet.generate_key()
    token = Fernet(key).encrypt(secret.encode())

    return FernetToken(token=token, key=key)
