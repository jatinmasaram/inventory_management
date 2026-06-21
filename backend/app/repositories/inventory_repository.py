from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


class InventoryRepository:

    def get_product_for_update(
        self,
        db: Session,
        product_id: int,
    ) -> Product | None:

        stmt = (
            select(Product)
            .where(Product.id == product_id)
            .with_for_update()
        )

        return db.scalar(stmt)

    def update_stock(
        self,
        db: Session,
        product: Product,
        new_stock: int,
    ) -> Product:

        product.stock_quantity = new_stock

        db.flush()

        return product