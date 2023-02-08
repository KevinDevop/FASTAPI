from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from Models.BSC_PAIS_MODEL import BSC_PAIS
from Schemas.BSC_PAIS import BSC_PAISSchema
from db import get_db


app = FastAPI()


# Crear la ruta GET


@app.get("/BSC_PAIS")
async def GetAllPais(db: Session = Depends(get_db)):
    paises = db.query(BSC_PAIS).all()
    return [BSC_PAISSchema(ID_PAIS=pais.id_pais, NOMB_PAIS=pais.nomb_pais) for pais in paises]


@app.get("/BSC_PAIS/{id_pais}")
async def GetPais(id_pais: int, db: Session = Depends(get_db)):
    user = db.query(BSC_PAIS).get(id_pais)
    return {"id": user.id_pais, "name": user.nomb_pais}
