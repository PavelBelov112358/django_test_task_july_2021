from functools import lru_cache

from pydantic import BaseSettings, validator, RedisDsn


class APPSettings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool
    ALLOWED_HOSTS: str

    POSTGRES_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    REDIS_BROKER_URL: RedisDsn

    @classmethod
    @validator('ALLOWED_HOSTS')
    def get_list_allowed_hosts(cls, v: str) -> list:
        return v.split(',')

    class Config:
        env_file = '.env'


@lru_cache()
def get_config() -> APPSettings:
    return APPSettings()


config = get_config()
