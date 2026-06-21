from decimal import Decimal

from pydantic import BaseModel, Field

from app.schemas.common import BaseSchema


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    sku: str = Field(..., min_length=2, max_length=100)
    price: Decimal = Field(..., gt=0)
    stock_quantity: int = Field(..., ge=0)


class ProductUpdate(BaseModel):
    name: str | None = None
    price: Decimal | None = Field(default=None, gt=0)
    stock_quantity: int | None = Field(default=None, ge=0)


class ProductResponse(BaseSchema):
    id: int
    name: str
    sku: str
    price: Decimal
    stock_quantity: int