from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Definir una clase que representa una tabla en la base de datos


class BSC_PAIS(Base):
    __tablename__ = "BSC_PAIS"
    id_pais = Column(Integer, primary_key=True, autoincrement=True)
    nomb_pais = Column(String)
    departamento = relationship(
        "BSC_DEPARTAMENTO", order_by="BSC_DEPARTAMENTO.ID_DEPARTAMETO", back_populates="pais")
