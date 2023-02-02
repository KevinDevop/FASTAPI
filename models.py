from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class BSC_PAIS(Base):
    __tablename__ = 'BSC_PAIS'
    ID_PAIS = Column(Integer, primary_key=True, index=True)
    NOMB_PAIS = Column(String(40), index=True)
