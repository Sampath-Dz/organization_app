from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

class BaseModel(Base):

    __abstract__=True

    id=Column(Integer,primary_key=True,index=True)

    created_at=Column(DateTime,default=datetime.utcnow)

    deleted_at=Column(DateTime,nullable=True)

