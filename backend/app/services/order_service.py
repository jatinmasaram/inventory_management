from decimal import Decimal

from sqlalchemy.orm import Session

from app.core.exceptions import (
    CustomerNotFoundException,
    OrderNotFoundException,
)
from app.models.order import (
    Order,
    OrderStatus,
)
from app.models.order_item import OrderItem
from app.repositories.customer_repository import (
    CustomerRepository,
)
from app.repositories.order_repository import (
    OrderRepository,
)
from app.schemas.order import OrderCreate
from app.services.inventory_service import (
    InventoryService,
)


class OrderService:

    def __init__(self):

        self.order_repository = (
            OrderRepository()
        )

        self.customer_repository = (
            CustomerRepository()
        )

        self.inventory_service = (
            InventoryService()
        )

    def create_order(
        self,
        db: Session,
        payload: OrderCreate,
    ) -> Order:

        customer = (
            self.customer_repository.get_by_id(
                db,
                payload.customer_id,
            )
        )

        if not customer:
            raise CustomerNotFoundException(
                f"Customer {payload.customer_id} not found"
            )

        total_amount = Decimal("0.00")

        order = Order(
            customer_id=payload.customer_id,
            total_amount=Decimal("0.00"),
            status=OrderStatus.PENDING,
        )

        self.order_repository.create(
            db,
            order,
        )

        for item in payload.items:

            product = (
                self.inventory_service.lock_product(
                    db,
                    item.product_id,
                )
            )

            self.inventory_service.validate_stock(
                product,
                item.quantity,
            )

            subtotal = (
                product.price *
                item.quantity
            )

            total_amount += subtotal

            old_stock = (
                product.stock_quantity
            )

            self.inventory_service.reduce_stock(
                db,
                product,
                item.quantity,
            )

            self.inventory_service.create_audit_log(
                db,
                product_id=product.id,
                old_stock=old_stock,
                new_stock=product.stock_quantity,
                reason=f"Order #{order.id}",
            )

            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=item.quantity,
                price_at_purchase=product.price,
                subtotal=subtotal,
            )

            self.order_repository.create_order_item(
                db,
                order_item,
            )

        order.total_amount = total_amount

        order.status = (
            OrderStatus.COMPLETED
        )

        db.flush()

        return order

    def get_order(
        self,
        db: Session,
        order_id: int,
    ):

        order = (
            self.order_repository.get_by_id(
                db,
                order_id,
            )
        )

        if not order:
            raise OrderNotFoundException(
                f"Order {order_id} not found"
            )

        return order

    def get_orders(
        self,
        db: Session,
    ):

        return self.order_repository.get_all(
            db
        )

    def delete_order(
        self,
        db: Session,
        order_id: int,
    ):

        order = self.get_order(
            db,
            order_id,
        )

        self.order_repository.delete(
            db,
            order,
        )