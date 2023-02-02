from fastapi import FastAPI, HTTPException
from database import SessioLocal
from sqlalchemy import text
from controllers import BSC_USUARIO

app = FastAPI()

app.include_router(BSC_USUARIO.router)


@app.get("/bscpais")
def bscpais():
    session = SessioLocal()
    query = text("SELECT * FROM BSC_PAIS")
    result = session.execute(query)
    rows = [dict(zip(result.keys(), row)) for row in result]
    return rows


@app.get("/bscdep/{id}")
def bscdep(id: str):
    rs = get_request(
        "SELECT * FROM BSC_DEPARTAMENTO WHERE ID_DEPARTAMENTO = "+id)
    if len(rs) > 0:
        return rs
    else:
        raise HTTPException(status_code=204)


@app.get('/mappract')
def bscpract():
    return get_request("SELECT * FROM MAP_PRACTICANTE")


def get_request(querystring: str):
    session = SessioLocal()
    query = text(querystring)
    result = session.execute(query)
    rows = [dict(zip(result.keys(), row)) for row in result]
    return rows


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
