from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False

# iniciando o fast
app = FastAPI()

produtos = [
    Produto(id=1, nome='PlayStation 5', preco=6000, em_oferta=True),
    Produto(id=2, nome='PlayStation 4', preco=3000, em_oferta=False),
    Produto(id=3, nome='XBox One', preco=3645.99, em_oferta=True),
    Produto(id=4, nome='Nintendo Wii', preco=1253.78, em_oferta=False),
    Produto(id=5, nome='Pc Gamer', preco=7000, em_oferta=False)
]

# rota 
@app.get('/')
async def index():
    return {'Teste': '123'}

@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None

@app.put('/produtos/{id}') # esse parametro vai na url 
async def atualizar_produto(id: int, produto: Produto): # parametro vai no corpo
    for prod in produtos:
        if prod.id == id:
            prod = produto

            return prod 
    return None