from pydantic import BaseModel


class BSC_PAISSchema(BaseModel):
    ID_PAIS: int
    NOMB_PAIS: str
