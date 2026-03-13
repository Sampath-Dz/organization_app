from sqlalchemy.orm import sessionmaker

from .models.db_base import engine


SessionLocal=sessionmaker(bind=engine)


def get_db():

    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()
