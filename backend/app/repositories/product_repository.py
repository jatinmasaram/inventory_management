from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    def create(
        self,
        db: Session,
        product: Product,
    ) -> Product:
        db.add(product)
        db.flush()
        db.refresh(product)
        return product

    def get_by_id(
        self,
        db: Session,
        product_id: int,
    ) -> Product | None:
        stmt = select(Product).where(
            Product.id == product_id
        )

        return db.scalar(stmt)

    def get_by_sku(
        self,
        db: Session,
        sku: str,
    ) -> Product | None:
        stmt = select(Product).where(
            Product.sku == sku
        )

        return db.scalar(stmt)

    def get_all(
        self,
        db: Session,
    ) -> list[Product]:
        stmt = select(Product)

        return list(
            db.scalars(stmt).all()
        )

    def delete(
        self,
        db: Session,
        product: Product,
    ) -> None:
        db.delete(product)

    def update(self, db: Session):
        db.flush()