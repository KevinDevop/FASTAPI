from sqlalchemy import Column, Integer, String, ForeignKey, DATE, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class BSC_USUARIO(Base):
    __tablename__ = 'BSC_USUARIO'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre_apellido_usuario = Column(String, nullable=False)
    cedula_usuario = Column(String, nullable=False)
    fecha_nacimiento = Column(DATE, nullable=False)
    correo_personal_usuario = Column(String, nullable=False)
    direccion_usuario = Column(String, nullable=False)
    estado_logico_usuario = Column(SmallInteger, nullable=False)
    telefono_usuario = Column(String, nullable=False)
    foto_usuario = Column(String)
    id_rol = Column(Integer, nullable=False)
    id_ciudad = Column(Integer, nullable=False)
    id_genero = Column(Integer, nullable=False)
    id_estado = Column(Integer, nullable=False)


class BSC_PAIS(Base):
    __tablename__ = "BSC_PAIS"
    id_pais = Column(Integer, primary_key=True, autoincrement=True)
    nomb_pais = Column(String)


class BSC_DEPARTAMENTO(Base):
    __tablename__ = 'BSC_DEPARTAMENTO'
    id_departamento = Column(Integer, primary_key=True, autoincrement=True)
    nombre_departamento = Column(String)
    id_pais = Column(Integer, ForeignKey('BSC_PAIS.id_pais'))
    pais = relationship("BSC_PAIS")


class BSC_CIUDAD(Base):
    __tablename__ = 'BSC_CIUDAD'
    id_ciudad = Column(Integer, primary_key=True)
    nombre_ciudad = Column(String, nullable=False)
    id_departamento = Column(Integer, ForeignKey(
        'BSC_DEPARTAMENTO.id_departamento'), nullable=False)
    departamento = relationship("BSC_DEPARTAMENTO")


class BSC_IDIOMA(Base):
    __tablename__ = 'BSC_IDIOMA'
    id_idioma = Column(Integer, primary_key=True, autoincrement=True)
    nombre_idioma = Column(String, nullable=False)


class BSC_USUARIO_IDIOMA(Base):
    __tablename__ = 'BSC_USUARIO_IDIOMA'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_idioma = Column(Integer, nullable=False)
    id_usuario = Column(Integer, nullable=False)


class MAP_PISO(Base):
    __tablename__ = 'MAP_PISO'
    id_piso = Column(Integer, primary_key=True, autoincrement=True)
    desc_piso = Column(String, nullable=False)


class MAP_ADMINISTRATIVO(Base):
    __tablename__ = "MAP_ADMINISTRATIVO"
    id_lider_administrativo = Column(
        Integer, primary_key=True, autoincrement=True)
    nombre_administrativo = Column(String, nullable=False)
