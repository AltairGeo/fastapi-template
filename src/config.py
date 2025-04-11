from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///database.db"
    token_lifetime: int = 3600 
    app_secret_reset_password: str
    app_secret_verify: str

    model_config = SettingsConfigDict(env_file=".env")


settings=Settings()

print(settings.db_url)