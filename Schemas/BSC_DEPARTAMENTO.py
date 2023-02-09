from pydantic import BaseModel


class BSC_DEPARTAMENTOSchema(BaseModel):
    ID_DEPARTAMENTO: int
    NOMBRE_DEPARTAMENTO: str
    ID_PAIS: int
