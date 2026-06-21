from fastapi import APIRouter, Depends
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.product import Product
from app.models.customer import Customer
from app.models.order import Order
from app.schemas.dashboard import DashboardResponse
from app.core.dependencies import (
    get_current_email,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/summary",
    response_model=DashboardResponse,
)
def get_dashboard_summary(
    db: Session = Depends(get_db),
    email: str = Depends(
        get_current_email
    ),
):

    total_products = db.scalar(
        select(func.count(Product.id))
    ) or 0

    total_customers = db.scalar(
        select(func.count(Customer.id))
    ) or 0

    total_orders = db.scalar(
        select(func.count(Order.id))
    ) or 0

    low_stock_products = db.scalar(
        select(func.count(Product.id))
        .where(Product.stock_quantity <= 10)
    ) or 0

    return {
        "total_products": total_products,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "low_stock_products": low_stock_products,
    }