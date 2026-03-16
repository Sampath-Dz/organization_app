from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .db_base import Base
from .base_model import BaseModel
from datetime import datetime

class Organization(BaseModel):
    __tablename__ = "organizations"

    name = Column(String, nullable=False, unique=True)
    teams = relationship("Team", back_populates="organization", cascade="all, delete-orphan")


class Team(BaseModel):
    __tablename__ = "teams"

    name = Column(String, nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    organization = relationship("Organization", back_populates="teams")
    members = relationship("Member", back_populates="team", cascade="all, delete-orphan")


class Member(BaseModel):
    __tablename__ = "members"

    name = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    team = relationship("Team", back_populates="members")
