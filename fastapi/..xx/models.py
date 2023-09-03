from pydantic import BaseModel
from typing import Optional

class Infos(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    endereco: Optional[str] = None
    