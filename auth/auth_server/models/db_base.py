from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

from ..settings import DATABASE_URL

Base = declarative_base()

engine = create_engine(DATABASE_URL)
