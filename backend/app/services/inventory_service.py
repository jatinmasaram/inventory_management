from sqlalchemy.orm import Session

from app.core.exceptions import (
    InsufficientStockException,
    ProductNotFoundException,
)
from app.models.inventory_audit import InventoryAudit
from app.models.product import Product
from app.repositories.inventory_repository import InventoryRepository


class InventoryService:

    def __init__(self):
        self.repository = InventoryRepository()

    def lock_product(
        self,
        db: Session,
        product_id: int,
    ) -> Product:

        product = self.repository.get_product_for_update(
            db,
            product_id,
        )

        if not product:
            raise ProductNotFoundException(
                f"Product {product_id} not found"
            )

        return product

    def validate_stock(
        self,
        product: Product,
        quantity: int,
    ) -> None:

        if product.stock_quantity < quantity:
            raise InsufficientStockException(
                f"Insufficient stock for product {product.id}"
            )

    def reduce_stock(
        self,
        db: Session,
        product: Product,
        quantity: int,
    ) -> Product:

        old_stock = product.stock_quantity

        new_stock = old_stock - quantity

        self.repository.update_stock(
            db,
            product,
            new_stock,
        )

        return product

    def create_audit_log(
        self,
        db: Session,
        product_id: int,
        old_stock: int,
        new_stock: int,
        reason: str,
    ) -> InventoryAudit:

        audit = InventoryAudit(
            product_id=product_id,
            old_stock=old_stock,
            new_stock=new_stock,
            reason=reason,
        )

        db.add(audit)

        return audit