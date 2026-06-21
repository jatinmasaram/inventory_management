from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.admin import Admin


class AdminRepository:

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> Admin | None:

        stmt = select(Admin).where(
            Admin.email == email
        )

        return db.scalar(stmt)

    def create(
        self,
        db: Session,
        admin: Admin,
    ) -> Admin:

        db.add(admin)

        db.commit()

        db.refresh(admin)

        return admin