from jose import jwt
from datetime import datetime, timedelta
import os

SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3


def createToken(id_usuario: int, expires_delta: timedelta):
    to_encode = {"ID": str(id_usuario),
                 "exp": datetime.utcnow() + expires_delta}
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt
