from pydantic_settings import BaseSettings, SettingsConfigDict

class MailSettings(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int = 587
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    model_config = SettingsConfigDict(env_file=".env")


class Settings(MailSettings, BaseSettings):
    db_url: str = "sqlite+aiosqlite:///database.db"
    token_lifetime: int = 3600 
    app_secret_reset_password: str
    app_secret_verify: str

    model_config = SettingsConfigDict(env_file=".env")

settings=Settings()


print(settings.db_url)