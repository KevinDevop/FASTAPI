from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from . import BSC_PAIS_MODEL

Base = declarative_base()

class BSC_DEPARTAMENTO(Base):
    __tablename__ = 'BSC_DEPARTAMENTO'
    id_departamento = Column(Integer, primary_key=True, autoincrement=True)
    nombre_departamento = Column(String)
    ID_PAIS = Column(Integer, ForeignKey('BSC_PAIS.ID_PAIS'))
    BSC_PAIS = relationship("BSC_PAIS", back_populates="BSC_DEPARTAMENTO")
    
BSC_PAIS_MODEL.BSC_PAIS.departamento = relationship("BSC_DEPARTAMENTO", order_by=BSC_DEPARTAMENTO.id_departamento, back_populates="BSC_PAIS") 