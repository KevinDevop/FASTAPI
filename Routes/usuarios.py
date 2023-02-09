from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db


route = APIRouter(prefix="/BSC_USUARIO", tags=["BSC_USUARIO"])


@route.get("/")
async def GetUsarios(db: Session = Depends(get_db)):
    usuarios = db.query()


