from typing import Any, Callable, Set

from pydantic import (
    AliasChoices,
    AmqpDsn,
    BaseModel,
    Field,
    ImportString,
    PostgresDsn,
    RedisDsn,
)

from pydantic_settings import BaseSettings, SettingsConfigDict




class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    
    OPENAI_API_KEY: str


settings = Settings()