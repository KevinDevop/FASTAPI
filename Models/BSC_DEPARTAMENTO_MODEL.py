from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


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
