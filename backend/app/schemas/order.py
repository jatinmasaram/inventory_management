from decimal import Decimal

from pydantic import BaseModel, Field

from app.schemas.common import BaseSchema


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class OrderCreate(BaseModel):
    customer_id: int
    items: list[OrderItemCreate]


class OrderResponse(BaseSchema):
    id: int
    customer_id: int
    total_amount: Decimal
    status: str