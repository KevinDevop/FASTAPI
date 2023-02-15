from fastapi import HTTPException, status


class NotFound(HTTPException):
    def __init__(self, id: int, message: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f"{message} con el id {id} no encontrado.")
