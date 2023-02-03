from fastapi import APIRouter
from . import defFunc


router = APIRouter()


@router.get('/mappract')
async def bscpract():
    return defFunc.get_request("SELECT * FROM MAP_PRACTICANTE")
