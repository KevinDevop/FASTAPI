from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from Models.Models import MAP_ADMINISTRATIVO
from Schemas.MAP_ADMINISTRATIVO import MAP_ADMINISTRATIVOSchema

route = APIRouter(prefix="/MAP_ADMINISTRATIVOS", tags=["MAP_ADMINISTRATIVOS"])


@route.get("/")
async def GetAdministrativos(db: Session = Depends(get_db)):
    administrativos = db.query(MAP_ADMINISTRATIVO).all()
    return [MAP_ADMINISTRATIVOSchema(ID_LIDER_ADMINISTRATIVO=admin.id_lider_administrativo, NOMBRE_ADMINISTRATIVO=admin.nombre_administrativo)for admin in administrativos]
