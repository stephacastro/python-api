from fastapi import FastAPI
from routes import curso_router 
from routes import usuario_router

app = FastAPI(title='API de Estudos', version='0.0.1', description='Uma API para meus estudos sobre FastApi')
app.include_router(curso_router.router, tags=['cursos']) # criando uma tag (rota) para agrupar todos os endpoints relacionados a um recurso
app.include_router(usuario_router.router, tags=['usuarios'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8000, debug=True, reload=True)