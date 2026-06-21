from sqlalchemy.orm import Session

from app.core.exceptions import (
    DuplicateSKUException,
    ProductNotFoundException,
)
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
)


class ProductService:

    def __init__(self):
        self.repository = ProductRepository()

    def create_product(
        self,
        db: Session,
        payload: ProductCreate,
    ) -> Product:

        existing_product = (
            self.repository.get_by_sku(
                db,
                payload.sku,
            )
        )

        if existing_product:
            raise DuplicateSKUException(
                f"SKU '{payload.sku}' already exists"
            )

        product = Product(
            name=payload.name,
            sku=payload.sku,
            price=payload.price,
            stock_quantity=payload.stock_quantity,
        )

        return self.repository.create(
            db,
            product,
        )

    def get_product(
        self,
        db: Session,
        product_id: int,
    ) -> Product:

        product = self.repository.get_by_id(
            db,
            product_id,
        )

        if not product:
            raise ProductNotFoundException(
                f"Product {product_id} not found"
            )

        return product

    def get_products(
        self,
        db: Session,
    ) -> list[Product]:

        return self.repository.get_all(db)

    def update_product(
        self,
        db: Session,
        product_id: int,
        payload: ProductUpdate,
    ) -> Product:

        product = self.get_product(
            db,
            product_id,
        )

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                product,
                field,
                value,
            )

        self.repository.update(
            db,
        )

        return product

    def delete_product(
        self,
        db: Session,
        product_id: int,
    ) -> None:

        product = self.get_product(
            db,
            product_id,
        )

        self.repository.delete(
            db,
            product,
        )