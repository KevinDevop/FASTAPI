from pydantic import BaseModel


class BSC_CIUDAD_SCHEMA(BaseModel):
    ID_CIUDAD: int
    NOMBRE_CIUDAD: str
    ID_DEPARTAMENTO: int


class BSC_CIUDAD_DEPARTAMENTO_SCHEMA(BaseModel):
    ID_CIUDAD: int
    NOMBRE_CIUDAD: str
    NOMBRE_DEPARTAMENTO : str