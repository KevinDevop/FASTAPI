from sqlalchemy import text
from database import SessioLocal


def get_request(querystring: str):
    session = SessioLocal()
    query = text(querystring)
    result = session.execute(query)
    rows = [dict(zip(result.keys(), row)) for row in result]
    return rows
