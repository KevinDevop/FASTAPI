from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import get_db
from Models.BSC_DEPARTAMENTO_MODEL import BSC_DEPARTAMENTO
from Schemas.BSC_DEPARTAMENTO import BSC_DEPARTAMENTOSchema

router = APIRouter(prefix="/BSC_DEPARTAMENTO", tags=["BSC_DEPARTAMENTO"])


@router.get("/{id_dep}")
async def GetDepartamento(id_dep: int, db: Session = Depends(get_db)):
    departameto = db.query(BSC_DEPARTAMENTO).filter(
        BSC_DEPARTAMENTO.id_departamento == id_dep).first()
    if departameto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No encontrado")
    return BSC_DEPARTAMENTOSchema(ID_DEPARTAMENTO=departameto.id_departamento, NOMBRE_DEPARTAMENTO=departameto.nombre_departamento, ID_PAIS=departameto.id_pais)
