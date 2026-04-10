from sqlmodel import create_engine, SQLModel

from app.register.model import User
from app.session.model import User_session

#creamos la maquina engine 
engine = create_engine("sqlite:///database_test.db")

def create_db_and_table():
    SQLModel.metadata.create_all(engine)