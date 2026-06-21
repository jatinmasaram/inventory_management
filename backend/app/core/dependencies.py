from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials


from jose import jwt
from jose import JWTError

from app.core.security import (
    SECRET_KEY,
    ALGORITHM,
)

security = HTTPBearer()


def get_current_email(
    credentials: HTTPAuthorizationCredentials =
    Depends(security),
):

    token = credentials.credentials


    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )


        email = payload.get("sub")

        if not email:

            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )

        return email

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )
    
def get_current_user(
    credentials: HTTPAuthorizationCredentials =
    Depends(security),
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        return {
            "email": payload.get("sub"),
            "role": payload.get("role"),
        }

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )
def require_admin(
    user=Depends(get_current_user),
):

    if user["role"] != "ADMIN":

        raise HTTPException(
            status_code=403,
            detail="Admin access required",
        )

    return user