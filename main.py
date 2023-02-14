from fastapi import FastAPI
from Routes import administrativos, departamento, pais, piso

app = FastAPI()

app.include_router(pais.routePais)
app.include_router(departamento.router)
app.include_router(administrativos.route)
app.include_router(piso.route)


@app.get("/")
async def default():
    return {"Message": "Hola"}
