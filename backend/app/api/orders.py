from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.order import (
    OrderCreate,
    OrderResponse,
)
from app.services.order_service import (
    OrderService,
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)

service = OrderService()


@router.post(
    "",
    response_model=OrderResponse,
    status_code=201,
)
def create_order(
    payload: OrderCreate,
    db: Session = Depends(get_db),
):

    order = service.create_order(
        db,
        payload,
    )

    db.commit()

    return order


@router.get(
    "",
    response_model=list[OrderResponse],
)
def get_orders(
    db: Session = Depends(get_db),
):

    return service.get_orders(db)


@router.get(
    "/{order_id}",
    response_model=OrderResponse,
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
):

    return service.get_order(
        db,
        order_id,
    )


@router.delete(
    "/{order_id}",
    status_code=204,
)
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
):

    service.delete_order(
        db,
        order_id,
    )

    db.commit()