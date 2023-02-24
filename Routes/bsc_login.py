from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import session
from db import get_db
from Models.Models import BSC_LOGIN
from Schemas.BSC_LOGIN import LoginCreateModel, BSC_LOGIN_SCHEMA, BSC_LOGIN_VERIFY_SCHEMA
from sendemail import codigoEmail
from bcrypt import gensalt, hashpw
from sqlalchemy.exc import SQLAlchemyError
import random

route = APIRouter(prefix="/BSC_LOGIN", tags=["BSC_LOGIN"])


@route.get("/", description="Lista los registro de bsc_login")
async def getLogin(db: session = Depends(get_db)):
    users = db.query(BSC_LOGIN).all()

    return [BSC_LOGIN_SCHEMA(
        ID_LOGIN=user.id_login,
        EMAIL_CORPORATIVO_LOGIN=user.email_corporativo_login,
        CONTRASEÑA_LOGIN=user.contraseña_login,
        ID_USUARIO=user.id_usuario,
        VERIFICACION_LOGIN=user.verificacion_login,
        COD_VERIFICACION_LOGIN=user.cod_verificacion_login)
        for user in users]


@route.put("/verificacion/{email}", description="Verificación de correo")
async def putVerificacionCorreo(verificacion: BSC_LOGIN_VERIFY_SCHEMA, email: str, db: session = Depends(get_db)):
    login = db.query(BSC_LOGIN).filter(
        BSC_LOGIN.email_corporativo_login == email).first()

    return login


@route.post("/", description="Crea un registro de un usuario")
async def registroLogin(login: LoginCreateModel, db: session = Depends(get_db)):
    salt = gensalt()
    hashed_password = hashpw(login.CONTRASEÑA_LOGIN.encode('utf-8'), salt)

    codigo_verificacion = ''.join(
        [str(random.randint(0, 9)) for _ in range(5)])

    db_registro = BSC_LOGIN(
        email_corporativo_login=login.EMAIL_CORPORATIVO_LOGIN,
        contraseña_login=hashed_password,
        id_usuario=login.ID_USUARIO,
        verificacion_login=True,
        cod_verificacion_login=codigo_verificacion
    )

    try:
        with db.begin():
            db.add(db_registro)
            db.flush()
            codigoEmail(login.EMAIL_CORPORATIVO_LOGIN, codigo_verificacion)
    except SQLAlchemyError as e:
        raise e

    return db_registro
