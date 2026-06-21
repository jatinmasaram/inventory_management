from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem


class OrderRepository:

    def create(
        self,
        db: Session,
        order: Order,
    ) -> Order:

        db.add(order)
        db.flush()

        return order

    def create_order_item(
        self,
        db: Session,
        order_item: OrderItem,
    ) -> OrderItem:

        db.add(order_item)
        db.flush()

        return order_item

    def get_by_id(
        self,
        db: Session,
        order_id: int,
    ) -> Order | None:

        stmt = (
            select(Order)
            .where(Order.id == order_id)
        )

        return db.scalar(stmt)

    def get_all(
        self,
        db: Session,
    ) -> list[Order]:

        stmt = select(Order)

        return list(
            db.scalars(stmt).all()
        )

    def delete(
        self,
        db: Session,
        order: Order,
    ):

        db.delete(order)