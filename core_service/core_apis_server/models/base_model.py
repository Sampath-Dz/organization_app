<<<<<<< HEAD
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

Base = declarative_base()

class BaseModel:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
=======
from sqlalchemy import Column,Integer,DateTime
from datetime import datetime

from .db_base import Base


class BaseModel(Base):

    __abstract__=True

    id=Column(Integer,primary_key=True,index=True)

    created_at=Column(DateTime,default=datetime.utcnow)

    deleted_at=Column(DateTime,nullable=True)
>>>>>>> 9073f23830fbf94017b86571b180ab41644f2c8b
