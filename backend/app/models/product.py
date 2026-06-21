from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    String,
    Numeric,
    DateTime,
    CheckConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    __table_args__ = (
        CheckConstraint(
            "stock_quantity >= 0",
            name="check_stock_non_negative",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    sku: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    stock_quantity: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="product",
    )

    inventory_audits: Mapped[list["InventoryAudit"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan",
    )