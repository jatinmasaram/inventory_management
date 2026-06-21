from decimal import Decimal

from sqlalchemy import (
    ForeignKey,
    Numeric,
    CheckConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    __table_args__ = (
        CheckConstraint(
            "quantity > 0",
            name="check_order_quantity_positive",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        nullable=False,
    )

    price_at_purchase: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    order: Mapped["Order"] = relationship(
        back_populates="items",
    )

    product: Mapped["Product"] = relationship(
        back_populates="order_items",
    )