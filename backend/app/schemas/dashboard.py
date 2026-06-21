from app.schemas.common import BaseSchema


class DashboardResponse(BaseSchema):
    total_products: int
    total_customers: int
    total_orders: int
    low_stock_products: int