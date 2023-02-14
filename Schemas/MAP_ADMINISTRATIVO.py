from pydantic import BaseModel


class MAP_ADMINISTRATIVOSchema(BaseModel):
    ID_LIDER_ADMINISTRATIVO: int
    NOMBRE_ADMINISTRATIVO: str
