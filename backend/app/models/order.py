from datetime import datetime
from decimal import Decimal
from enum import Enum

from sqlalchemy import (
    DateTime,
    Enum as SqlEnum,
    ForeignKey,
    Numeric,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class OrderStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id", ondelete="CASCADE"),
        nullable=False,
    )

    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=0,
    )

    status: Mapped[OrderStatus] = mapped_column(
        SqlEnum(OrderStatus),
        nullable=False,
        default=OrderStatus.PENDING,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="orders",
    )

    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
    )