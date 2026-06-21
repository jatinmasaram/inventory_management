from datetime import datetime
from datetime import timedelta

from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

SECRET_KEY = settings.JWT_SECRET_KEY

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(
    password: str,
) -> str:

    return pwd_context.hash(
        password
    )


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:

    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(
    subject: str,
    role : str,
) -> str:

    expire = (
        datetime.utcnow()
        + timedelta(
            minutes=
            ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": subject,
        "role" : role, 
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )