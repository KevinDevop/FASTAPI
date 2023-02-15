from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from Models.Models import BSC_CIUDAD, BSC_DEPARTAMENTO
from Schemas.BSC_CIUDAD import BSC_CIUDAD_SCHEMA, BSC_CIUDAD_DEPARTAMENTO_SCHEMA
from db import get_db


route = APIRouter(prefix="/BSC_CIUDAD", tags=["BSC_CIUDAD"])


@route.get("/", description="Retorna todas las ciudades")
async def getCiudad(db: Session = Depends(get_db)):
    ciudades = db.query(BSC_CIUDAD).all()

    return [BSC_CIUDAD_SCHEMA(ID_CIUDAD=ciudad.id_ciudad, NOMBRE_CIUDAD=ciudad.nombre_ciudad, ID_DEPARTAMENTO=ciudad.id_departamento)for ciudad in ciudades]


@route.get("/DEPARTAMENTO", description="Retorna todas las ciuidades con su respectivo departamento")
async def GetCiudadesDepartameto(db: Session = Depends(get_db)):
    ciudades = db.query(BSC_CIUDAD, BSC_DEPARTAMENTO).join(
        BSC_DEPARTAMENTO, BSC_CIUDAD.id_departamento == BSC_DEPARTAMENTO.id_departamento).all()

    result = [BSC_CIUDAD_DEPARTAMENTO_SCHEMA(ID_CIUDAD=ciudad.id_ciudad, NOMBRE_CIUDAD=ciudad.nombre_ciudad,
                                             NOMBRE_DEPARTAMENTO=departamento.nombre_departamento) for ciudad, departamento in ciudades]

    return result
