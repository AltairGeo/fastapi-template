from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///database.db"
    token_lifetime: int = 3600 

    model_config = SettingsConfigDict(env_file=".env")


settings=Settings()

print(settings.db_url)