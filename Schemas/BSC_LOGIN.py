from pydantic import BaseModel, EmailStr


class BSC_LOGIN_SCHEMA(BaseModel):
    ID_LOGIN: int
    EMAIL_CORPORATIVO_LOGIN: str
    CONTRASEÑA_LOGIN: str
    ID_USUARIO: int
    VERIFICACION_LOGIN: str
    COD_VERIFICACION_LOGIN: str


class LoginCreateModel(BaseModel):
    EMAIL_CORPORATIVO_LOGIN: str
    CONTRASEÑA_LOGIN: str
    ID_USUARIO: int
