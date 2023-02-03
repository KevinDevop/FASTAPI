from fastapi import APIRouter
from . import defFunc

router = APIRouter()


@router.get("/bscpais")
async def bscpais():
    return defFunc.get_request("SELECT * FROM BSC_PAIS")
