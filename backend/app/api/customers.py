from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse,
)
from app.services.customer_service import (
    CustomerService,
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)

service = CustomerService()


@router.post(
    "",
    response_model=CustomerResponse,
    status_code=201,
)
def create_customer(
    payload: CustomerCreate,
    db: Session = Depends(get_db),
):
    customer = service.create_customer(
        db,
        payload,
    )

    db.commit()

    return customer


@router.get(
    "",
    response_model=list[CustomerResponse],
)
def get_customers(
    db: Session = Depends(get_db),
):
    return service.get_customers(db)


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db),
):
    return service.get_customer(
        db,
        customer_id,
    )


@router.delete(
    "/{customer_id}",
    status_code=204,
)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db),
):
    service.delete_customer(
        db,
        customer_id,
    )

    db.commit()