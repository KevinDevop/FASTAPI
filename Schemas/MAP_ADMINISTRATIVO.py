from pydantic import BaseModel


class MAP_ADMINISTRATIVOSchema(BaseModel):
    ID_LIDER_ADMINISTRATIVO: int
    NOMBRE_ADMINISTRATIVO: str

class MAP_ADMINISTRATIVOS_POST_SCHEMA(BaseModel):
    NOMBRE_ADMINISTRATIVO : str