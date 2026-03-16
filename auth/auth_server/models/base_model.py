from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from .db_base import Base


class BaseModel(Base):

    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    created_at = Column(DateTime, server_default=func.now())

    deleted_at = Column(DateTime, nullable=True)
