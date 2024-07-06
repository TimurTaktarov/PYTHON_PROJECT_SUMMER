from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = f"Fastapi project TTR"


def get_settings():
    return Settings()


settings = get_settings()