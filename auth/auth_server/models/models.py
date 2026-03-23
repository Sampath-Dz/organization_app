import uuid
import time
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from auth.auth_server.models.db_base import Base


def generate_uuid():
    return str(uuid.uuid4())


def current_timestamp():
    return int(time.time())


class BaseModel(Base):
    __abstract__ = True

    id = Column(String, primary_key=True, default=generate_uuid)
    created_at = Column(Integer, nullable=False, default=current_timestamp)
    deleted_at = Column(Integer, nullable=True)


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String(100), nullable=False)
    mail = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    last_login = Column(Integer, nullable=True)

    assignments = relationship("Assignment", back_populates="user")


class Role(BaseModel):
    __tablename__ = "roles"

    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)

    assignments = relationship("Assignment", back_populates="role")


class Type(BaseModel):
    __tablename__ = "types"

    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)

    assignments = relationship("Assignment", back_populates="type")


class Assignment(BaseModel):
    __tablename__ = "assignments"

    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    role_id = Column(String, ForeignKey("roles.id"), nullable=False)
    type_id = Column(String, ForeignKey("types.id"), nullable=False)
    resource_id = Column(String, nullable=True)

    user = relationship("User", back_populates="assignments")
    role = relationship("Role", back_populates="assignments")
    type = relationship("Type", back_populates="assignments")