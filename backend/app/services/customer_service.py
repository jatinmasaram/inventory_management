from sqlalchemy.orm import Session

from app.core.exceptions import (
    CustomerNotFoundException,
    DuplicateEmailException,
)
from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer import CustomerCreate


class CustomerService:

    def __init__(self):
        self.repository = CustomerRepository()

    def create_customer(
        self,
        db: Session,
        payload: CustomerCreate,
    ) -> Customer:

        existing_customer = (
            self.repository.get_by_email(
                db,
                payload.email,
            )
        )

        if existing_customer:
            raise DuplicateEmailException(
                f"Email '{payload.email}' already exists"
            )

        customer = Customer(
            full_name=payload.full_name,
            email=payload.email,
            phone=payload.phone,
        )

        return self.repository.create(
            db,
            customer,
        )

    def get_customer(
        self,
        db: Session,
        customer_id: int,
    ) -> Customer:

        customer = self.repository.get_by_id(
            db,
            customer_id,
        )

        if not customer:
            raise CustomerNotFoundException(
                f"Customer {customer_id} not found"
            )

        return customer

    def get_customers(
        self,
        db: Session,
    ) -> list[Customer]:

        return self.repository.get_all(db)

    def delete_customer(
        self,
        db: Session,
        customer_id: int,
    ) -> None:

        customer = self.get_customer(
            db,
            customer_id,
        )

        self.repository.delete(
            db,
            customer,
        )