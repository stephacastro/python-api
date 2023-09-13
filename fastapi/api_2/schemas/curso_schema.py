from typing import Optional
from pydantic import BaseModel as SCBaseModel


class CursoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    aula: int
    horas: int

    class Config:
        orm_mode = True