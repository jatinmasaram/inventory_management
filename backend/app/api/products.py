from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.core.dependencies import (
    get_current_user,
    require_admin   
)

from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
)

from app.services.product_service import (
    ProductService,
)

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)

service = ProductService()


@router.post(
    "",
    response_model=ProductResponse,
    status_code=201,
)
def create_product(
    payload: ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(require_admin),
):
    product = service.create_product(
        db,
        payload,
    )

    db.commit()

    return product


@router.get(
    "",
    response_model=list[ProductResponse],
)
def get_products(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return service.get_products(db)


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return service.get_product(
        db,
        product_id,
    )


@router.put(
    "/{product_id}",
    response_model=ProductResponse,
)
def update_product(
    product_id: int,
    payload: ProductUpdate,
    db: Session = Depends(get_db),
    user=Depends(require_admin),
):
    product = service.update_product(
        db,
        product_id,
        payload,
    )

    db.commit()

    return product


@router.delete(
    "/{product_id}",
    status_code=204,
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_admin),
):
    service.delete_product(
        db,
        product_id,
    )

    db.commit()