from dataclasses import field
from datetime import date, datetime
from sqlmodel import Field, SQLModel  

#entidad session
class Session(SQLModel, table=True):
    usuario_id: int = Field(foreign_key="user.id")
    date_inicio : datetime =Field(default= datetime.now())
    date_fin : datetime = Field(default= datetime.now())