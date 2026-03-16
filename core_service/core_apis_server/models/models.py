from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .db_base import Base  

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    teams = relationship("Team", back_populates="organization", cascade="all, delete-orphan")


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    organization_id = Column(Integer, ForeignKey("organizations.id"))
    organization = relationship("Organization", back_populates="teams")

    members = relationship("Member", back_populates="team", cascade="all, delete-orphan")


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="members")
