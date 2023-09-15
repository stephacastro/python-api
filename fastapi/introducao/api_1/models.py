from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo') # utilizando o validator para criar uma condição de validação
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras')
        
        if value.islower():
            raise ValueError('O título deve ser capitalizado.')
        
        return value

cursos = [
    Curso(id=1, titulo='Programação com Python', aulas=78, horas=100),
    Curso(id=2, titulo='Lógica de Programação', aulas=53,  horas=70)
]

