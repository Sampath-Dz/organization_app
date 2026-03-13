from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from .db_base import Base

class BaseModel(Base):

    __abstract__ = True

    id = Column(Integer, primary_key=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    deleted_at = Column(DateTime, nullable=True)
