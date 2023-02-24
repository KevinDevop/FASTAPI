from fastapi import FastAPI
from Routes import bsc_departamento, bsc_pais, bsc_idioma, bsc_usuario, bsc_ciudad, map_administrativos, map_piso, map_practicante, bsc_login

app = FastAPI()

app.include_router(bsc_usuario.route)
app.include_router(bsc_pais.route)
app.include_router(bsc_departamento.route)
app.include_router(bsc_ciudad.route)
app.include_router(map_administrativos.route)
app.include_router(map_piso.route)
app.include_router(bsc_idioma.route)
app.include_router(map_practicante.route)
app.include_router(bsc_login.route)


@app.get("/")
async def default():
    return {"Message": "Hola"}
