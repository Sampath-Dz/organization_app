from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from core_service.core_apis_server.models.db_base import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)


class Organization(BaseModel):
    __tablename__ = "organizations"

    name = Column(String, nullable=False, unique=True)
    teams_count = Column(Integer, default=0)
    members_count = Column(Integer, default=0)

    teams = relationship(
        "Team",
        back_populates="organization",
        cascade="all, delete-orphan"
    )


class Team(BaseModel):
    __tablename__ = "teams"

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False
    )

    parent_id = Column(
        Integer,
        ForeignKey("teams.id"),
        nullable=True
    )

    organization = relationship(
        "Organization",
        back_populates="teams"
    )

    members = relationship(
        "Member",
        back_populates="team",
        cascade="all, delete-orphan"
    )


class Member(BaseModel):
    __tablename__ = "members"

    team_id = Column(
        Integer,
        ForeignKey("teams.id"),
        nullable=False
    )

    auth_user_id = Column(Integer, nullable=False)

    team = relationship(
        "Team",
        back_populates="members"
    )
