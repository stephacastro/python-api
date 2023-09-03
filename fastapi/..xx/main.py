from fastapi import FastAPI
from models import Infos
from fastapi import HTTPException
from fastapi import status
from typing import Optional

app = FastAPI()

infos = {
    
    1: {
        "nome": "Marcelo", "idade": 38, "endereco": "Rua do Amor, 1109"
    },

    2: {
        "nome": "Carolina", "idade": 23, "endereco": "Avenida do Estado, 100"
    },

    3: {
        "nome": "Emanuel", "idade": 18, "endereco": "Costa do Amaral, 98"
    }
}

# trazendo todos os dados
@app.get('/infos')
async def get_infos():
    return infos

@app.get('/infos/{infos_id}')
async def get_infos(infos_id: int):
    try:
        info = infos[infos_id]
        return info
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Informação não encontrada.')

@app.get('/infos/{infos_endereco}')
async def get_endereco(infos_id: int, endereco: Infos):
    if infos_id in infos_id:
        infos[endereco] = endereco
        return endereco
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Endereço não encontrado')



