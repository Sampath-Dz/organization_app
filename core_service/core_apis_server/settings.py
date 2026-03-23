import os
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    DB_HOST: str = "ep-polished-fog-a1k46pru-pooler.ap-southeast-1.aws.neon.tech"
    DB_PORT: int = 5432
    DB_USER: str = "neondb_owner"
    DB_PASSWORD: str = "npg_c32QXDIlRkqV"
    DB_NAME: str = "organization_app"

    AUTH_SERVICE_URL: str = "http://localhost:8001"
    JWT_SECRET: str = "supersecret"
    JWT_ALGO: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    CORE_APP_TITLE: str = "Core Service"
    CORE_APP_VERSION: str = "1.0.0"
    CORE_APP_HOST: str = "127.0.0.1"
    CORE_APP_PORT: int = 8002
    CORE_DEBUG: bool = True

    CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?sslmode=require"
        )

settings = Settings()