from fastapi import FastAPI # importando a classe principal

# instânciando o objeto (se torna um decorator)
app = FastAPI()

# 
@app.get('/') # ('/qualquercoisa') endpoint
async def mensagem():
    return {"msg": "Aprendendo FastApi..."}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", 
                port=8000, log_level="info", reload=True)