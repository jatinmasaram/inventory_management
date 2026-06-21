from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class InventoryAudit(Base):
    __tablename__ = "inventory_audit_logs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False,
    )

    old_stock: Mapped[int] = mapped_column(
        nullable=False,
    )

    new_stock: Mapped[int] = mapped_column(
        nullable=False,
    )

    reason: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    product: Mapped["Product"] = relationship(
        back_populates="inventory_audits",
    )