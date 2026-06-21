from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    DEBUG: bool = False
    API_PREFIX: str

    DATABASE_URL: str
    REDIS_URL: str
    REDIS_HOST: str
    REDIS_PORT: int

    RATE_LIMIT: int = 100
    LOG_LEVEL: str = "INFO"
    JWT_SECRET_KEY: str 

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()