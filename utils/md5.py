from passlib.context import CryptContext
from passlib.hash import md5_crypt
import hashlib

m = hashlib.md5()


# pwd_cxt = CryptContext(schemes="md5", deprecated="auto")


class Hash:
    def md5crypt(password: str):
        return hashlib.md5(password)

    def verify(hashed_password: str, plain_password: str):
        h = hashlib.md5(plain_password.encode())
        your_password = h.hexdigest()
        if hashed_password == your_password:
            return True
        else:
            return False
