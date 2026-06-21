from fastapi import APIRouter
from fastapi import Depends

from app.core.dependencies import (
    get_current_user,
)

router = APIRouter(
    prefix="/test",
    tags=["Test"],
)


@router.get("/me")
def me(
    email: str = Depends(
        get_current_user
    )
):
    return {
        "email": email
    }