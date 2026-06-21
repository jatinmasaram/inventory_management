from pydantic import BaseModel, EmailStr, Field

from app.schemas.common import BaseSchema


class CustomerCreate(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=255)
    email: EmailStr
    phone: str = Field(..., min_length=8, max_length=20)


class CustomerResponse(BaseSchema):
    id: int
    full_name: str
    email: str
    phone: str