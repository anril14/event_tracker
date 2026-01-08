import os
from dotenv import load_dotenv

from pydantic.v1 import BaseSettings

load_dotenv()


# TODO: Рефакторинг на pydantic модель
class Settings:

    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.dbname = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')

    @property
    def url_psycopg(self) -> str:
        return f'postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}'

    @property
    def url_asyncpg(self) -> str:
        return f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}'


settings = Settings()
