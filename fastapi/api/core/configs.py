from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base # herda todos os recursos do sql model
from typing import ClassVar

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str =  'postgresql+asyncpg://postgres:tete.1.2@localhost:5432/faculdade'
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()