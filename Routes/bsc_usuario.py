from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from Models.Models import BSC_USUARIO
from Schemas.BSC_USUARIO import BSC_USUARIO_SCHEMA
from db import get_db


route = APIRouter(prefix="/BSC_USUARIO", tags=["BSC_USUARIO"])


@route.get("/")
async def getUsuario(db: Session = Depends(get_db)):
    usuarios = db.query(BSC_USUARIO).all()

    return [BSC_USUARIO_SCHEMA(ID_USUARIO=usuario.id_usuario, NOMBRE_APELLIDO_USUARIO=usuario.nombre_apellido_usuario, CEDULA_USUARIO=usuario.cedula_usuario, FECHA_NACIMIENTO=usuario.fecha_nacimiento, CORREO_PERSONAL_USUARIO=usuario.correo_personal_usuario, DIRECCION_USUARIO=usuario.direccion_usuario, ESTADO_LOGICO_USUARIO=usuario.estado_logico_usuario, TELEFONO_USUARIO=usuario.telefono_usuario, FOTO_USUARIO=usuario.foto_usuario, ID_ROL=usuario.id_rol, ID_CIUDAD=usuario.id_ciudad, ID_GENERO=usuario.id_genero, ID_ESTADO=usuario.id_estado)for usuario in usuarios]
