from fastapi import APIRouter, HTTPException
from . import defFunc


router = APIRouter(prefix="/bscdep", tags={"BSC_DEPARTAMENTO"},
                   responses={404: {'message': 'No Encontrado'}})


@router.get('/')
async def bscdep():
    return defFunc.get_request("SELECT * FROM BSC_DEPARTAMENTO")


@router.get("/{id}")
async def bscdep(id: str):
    rs = defFunc.get_request(
        "SELECT * FROM BSC_DEPARTAMENTO WHERE ID_DEPARTAMENTO = "+id)
    if len(rs) > 0:
        return rs
    else:
        raise HTTPException(status_code=204)
