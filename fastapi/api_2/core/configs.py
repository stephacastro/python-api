from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base # herda todos os recursos do sql model

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str =  'postgresql+asyncpg://postgres:tete.1.2@localhost:5432/faculdade'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()