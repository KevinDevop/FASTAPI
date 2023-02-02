from fastapi import APIRouter
from sqlalchemy import text
from database import SessioLocal

router = APIRouter()


@router.get('/bscusuario')
def getBscUsuario():
    return get_request('SELECT * FROM BSC_USUARIO')


def get_request(querystring: str):
    session = SessioLocal()
    query = text(querystring)
    result = session.execute(query)
    rows = [dict(zip(result.keys(), row)) for row in result]
    return rows
