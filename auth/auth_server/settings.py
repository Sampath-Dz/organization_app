import os
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    JWT_SECRET: str
    JWT_ALGO: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    CORE_APP_TITLE: str = "Core Service"
    CORE_APP_VERSION: str = "1.0.0"
    CORE_APP_HOST: str = "127.0.0.1"
    CORE_APP_PORT: int = 8002
    CORE_DEBUG: bool = True

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?sslmode=require"
        )

settings = Settings()