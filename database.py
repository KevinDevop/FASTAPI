from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQL_ALCHEMY_DATABASE_URL = ("mssql+pyodbc://sa:1234@3420-KOSORIO\SQLEXPRESS/Control_Asistencia"
                            "?driver=ODBC+Driver+17+for+SQL+Server")

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessioLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

