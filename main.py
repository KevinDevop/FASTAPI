from fastapi import FastAPI
from Routes import pais, departamento


app = FastAPI()

app.include_router(pais.routePais)
app.include_router(departamento.router)


@app.get("/")
async def default():
    return {"Message": "Hola"}

# @app.get('/')
# async def GetAllPais(db: Session = Depends(get_db)):
#     paises = db.query(BSC_PAIS).all()
#     return [BSC_PAISSchema(ID_PAIS=pais.id_pais, NOMB_PAIS=pais.nomb_pais) for pais in paises]


# @app.get("/{id_pais}")
# async def GetPais(id_pais: int, db: Session = Depends(get_db)):
#     user = db.query(BSC_PAIS).get(id_pais)
#     return {"id": user.id_pais, "name": user.nomb_pais}
