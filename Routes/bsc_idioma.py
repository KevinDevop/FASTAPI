from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from Models.Models import BSC_IDIOMA
from Schemas.BSC_IDIOMA import BSC_IDIOMA_SCHEMA
from db import get_db


route = APIRouter(prefix="/BSC_IDIOMA", tags=["BSC_IDIOMAS"])


@route.get('/', description="Retorna los idiomas ❤️")
async def getIdiomas(db: Session = Depends(get_db)):
    idiomas = db.query(BSC_IDIOMA).all()
    return [BSC_IDIOMA_SCHEMA(ID_IDIOMA=idioma.id_idioma, NOMBRE_IDIOMA=idioma.nombre_idioma)for idioma in idiomas]
