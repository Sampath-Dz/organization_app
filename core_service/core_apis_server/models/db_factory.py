from core_service.core_apis_server.models.db_base import BaseDB
from core_service.core_apis_server.settings import settings

class DBFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            instance = super().__new__(cls)
            db_url = (
                f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}"
                f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?sslmode=require"
            )
            instance.db = BaseDB(db_url)
            cls._instance = instance
        return cls._instance

    def get_db(self):
        session = self.db.session()
        try:
            yield session
        finally:
            session.remove()

postgres_db = DBFactory().db