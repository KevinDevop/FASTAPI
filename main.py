from fastapi import FastAPI
from Routes import administrativos, departamento, pais, piso, bsc_idioma, bsc_usuario, bsc_ciudad

app = FastAPI()

app.include_router(bsc_usuario.route)
app.include_router(pais.route)
app.include_router(departamento.route)
app.include_router(bsc_ciudad.route)
app.include_router(administrativos.route)
app.include_router(piso.route)
app.include_router(bsc_idioma.route)


@app.get("/")
async def default():
    return {"Message": "Hola"}
