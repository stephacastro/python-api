from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo='Programação com Python', aulas=78, horas=100),
    Curso(id=2, titulo='Lógica de Programação', aulas=53,  horas=70)
]

