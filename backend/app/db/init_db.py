from app.db.base import Base
from app.db.session import engine

# Import all models
from app.models import *


# def create_tables():
#     Base.metadata.create_all(bind=engine)