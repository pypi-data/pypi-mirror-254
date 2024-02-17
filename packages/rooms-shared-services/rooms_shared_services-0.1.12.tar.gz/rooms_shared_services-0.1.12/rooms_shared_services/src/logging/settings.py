from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

LevelLiteral = Literal["DEBUG", "INFO", "WARN", "ERROR"]


class Settings(BaseSettings):
    """HTTP logging settings."""

    model_config = SettingsConfigDict(env_prefix="http_logging_")

    host: str = "cfribc1wdc.execute-api.us-east-1.amazonaws.com"
    path: str = "/handle-logs"
    secure: bool = True
    loglevel: LevelLiteral = "INFO"
