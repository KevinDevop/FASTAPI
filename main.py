from fastapi import FastAPI
from routers import BSC_USUARIO, BSC_PAIS, MAP_PARTICANTES, BSC_DEPARTAMENTO

app = FastAPI()

app.include_router(BSC_USUARIO.router)
app.include_router(BSC_PAIS.router)
app.include_router(MAP_PARTICANTES.router)
app.include_router(BSC_DEPARTAMENTO.router)

# class Item(BaseSQL):
#     __tablename__ = "BSC_PAIS"
#     ID_PAIS = Column(Integer, primary_key=True, index=True)
#     NOMB_PAIS = Column(String, index=True)


# def create_item(db, item):
#     db.add(item)

# @app.post("/POST_PAIS/")
# async def post_pais(item: Item):
#     db = SessioLocal()
#     create_item(db, item)
#     db.commit()
#     db.close()
