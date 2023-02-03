from fastapi import APIRouter
from . import defFunc

router = APIRouter()


@router.get('/bscusuario')
async def getBscUsuario():
    return defFunc.get_request('SELECT * FROM BSC_USUARIO')