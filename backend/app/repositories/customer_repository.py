from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.customer import Customer


class CustomerRepository:

    def create(
        self,
        db: Session,
        customer: Customer,
    ) -> Customer:
        db.add(customer)
        db.flush()
        db.refresh(customer)
        return customer

    def get_by_id(
        self,
        db: Session,
        customer_id: int,
    ) -> Customer | None:
        stmt = select(Customer).where(
            Customer.id == customer_id
        )

        return db.scalar(stmt)

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> Customer | None:
        stmt = select(Customer).where(
            Customer.email == email
        )

        return db.scalar(stmt)

    def get_all(
        self,
        db: Session,
    ) -> list[Customer]:
        stmt = select(Customer)

        return list(
            db.scalars(stmt).all()
        )

    def delete(
        self,
        db: Session,
        customer: Customer,
    ) -> None:
        db.delete(customer)