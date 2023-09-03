from typing import List, Optional, Any
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Response
from models import Curso
from fastapi import Path
from fastapi import Query
from fastapi import Header
from time import sleep
from fastapi import Depends


# Simulando um banco para injetar dependência
def fake_db():
    try:
        print('Abrindo conexão com banco de dados')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados')
        sleep(1)

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação com Python",
        "aulas": 78,
        "horas": 100
    },

    2: {
        "titulo": "Power BI",
        "aulas": 53,
        "horas": 70
    }
}

# trás os recursos
@app.get('/cursos')
async def get_cursos(db: Any=Depends(fake_db)): # passando a depência da conexão do banco para que essa função execute
    return cursos 

@app.get('/cursos/{curso_id}')      # utilizando o path para limitar um range de id a serem aceitos     
async def get_curso(curso_id: int = Path(default=None, title='ID do Curso', description='Deve ser entre 1 e 2.', gt=0, lt=3), db: Any=Depends(fake_db)):
    try: # tradando exeções
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

 # cria/adiciona novos recursos   
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any=Depends(fake_db)):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

# atualiza recursos
@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any=Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id {curso_id}')
    
@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any=Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTEN)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id {curso_id}')

########################## QUERY PARAMETERS E HEADER ##########################
@app.get('/calculadora')
async def calculadora(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_teste: str = Header(default=None), c: Optional[int] = None ):
    soma: int = a + b
    if c:
        soma = soma + c
    print(f'X-Teste: {x_teste}')

    return {"resultado": soma}
###############################################################################

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000, debug=True, reload=True)