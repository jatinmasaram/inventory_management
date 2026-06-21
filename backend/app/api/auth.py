from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
)

from app.services.auth_service import (
    AuthService,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

service = AuthService()


@router.post("/register")
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db),
):

    return service.register(
        db,
        payload.email,
        payload.password,
    )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db),
):

    return service.login(
        db,
        payload.email,
        payload.password,
    )