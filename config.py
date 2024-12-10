from pydantic_settings import BaseSettings


class BotConfig(BaseSettings):
    BOT_TOKEN: str
    ADMIN_ID: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = BotConfig()
