from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    verify_password,
)

from app.core.exceptions import (
    UnauthorizedException,DuplicateEmailException
)

from app.repositories.admin_repository import (
    AdminRepository,
)

from app.models.admin import Admin

from app.core.security import (
    hash_password,
)


class AuthService:

    def __init__(self):

        self.repository = (
            AdminRepository()
        )
    def register(
        self,
        db: Session,
        email: str,
        password: str,
    ):

        existing = (
            self.repository.get_by_email(
                db,
                email,
            )
        )

        if existing:

            raise DuplicateEmailException(
                "Email already registered"
            )

        admin = Admin(
            email=email,
            hashed_password=hash_password(
                password
            ),
            role="ADMIN",
        )

        admin = self.repository.create(db,admin,)
        token = create_access_token(admin.email,admin.role,)

        return{"access_token":token,"token_type":"bearer","user":{
            "id":admin.id,"email":admin.email,"role":admin.role,
        }
    }


    def login(
        self,
        db: Session,
        email: str,
        password: str,
    ):
        


        admin = (
            self.repository.get_by_email(
                db,
                email,
            )
            
        )
        

        # if admin:
        #     print(
        #         "HASH =",
        #         admin.hashed_password
        #     )

            # print("VERIFY =",verify_password(password,admin.hashed_password,))

        if not admin:

            raise UnauthorizedException(
                "Invalid credentials"
            )

        if not verify_password(
            password,
            admin.hashed_password,
        ):

            raise UnauthorizedException(
                "Invalid credentials"
            )

        token = (
            create_access_token(
                admin.email,
                admin.role,
            )
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
            "id": admin.id,
            "email": admin.email,
            "role": admin.role,
            }
        }