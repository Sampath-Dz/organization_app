from sqlalchemy.orm import declarative_base
<<<<<<< HEAD

Base = declarative_base()
=======
from sqlalchemy import create_engine

from ..settings import DATABASE_URL


Base = declarative_base()

engine = create_engine(DATABASE_URL)
>>>>>>> 9073f23830fbf94017b86571b180ab41644f2c8b
