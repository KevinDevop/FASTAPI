from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routes import bsc_departamento, bsc_pais, bsc_idioma, bsc_usuario, bsc_ciudad, map_administrativos, map_piso, map_practicante, bsc_login, bsc_bitacora
from db import get_db

app = FastAPI()

origin = [
    "http://localhost:5173",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(bsc_usuario.route)
app.include_router(bsc_pais.route)
app.include_router(bsc_departamento.route)
app.include_router(bsc_ciudad.route)
app.include_router(map_administrativos.route)
app.include_router(map_piso.route)
app.include_router(bsc_idioma.route)
app.include_router(map_practicante.route)
app.include_router(bsc_login.route)
app.include_router(bsc_bitacora.route)


@app.get("/")
async def default():
    return {"Message": "Hola"}


@app.middleware("http")
async def db_session_middleware(request, call_next):
    request.state.db = next(get_db())
    response = await call_next(request)
    return response
