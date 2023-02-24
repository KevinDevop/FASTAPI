from fastapi import FastAPI
from Routes import administrativos, departamento, pais, piso, bsc_idioma, bsc_usuario, bsc_ciudad, map_practicante, bsc_bitacora

app = FastAPI()

app.include_router(bsc_usuario.route)
app.include_router(pais.route)
app.include_router(departamento.route)
app.include_router(bsc_ciudad.route)
app.include_router(administrativos.route)
app.include_router(piso.route)
app.include_router(bsc_idioma.route)
app.include_router(map_practicante.route)
app.include_router(bsc_bitacora.route)


@app.get("/")
async def default():
    return {"Message": "Hola"}
