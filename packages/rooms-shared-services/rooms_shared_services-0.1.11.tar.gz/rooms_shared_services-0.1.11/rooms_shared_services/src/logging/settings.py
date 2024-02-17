from typing import Literal

from pydantic_settings import BaseSettings

LevelLiteral = Literal["DEBUG", "INFO", "WARN", "ERROR"]


class Settings(BaseSettings):
    host: str = "cfribc1wdc.execute-api.us-east-1.amazonaws.com"
    path: str = "/handle-logs"
    secure: bool = True
    loglevel: LevelLiteral = "INFO"
