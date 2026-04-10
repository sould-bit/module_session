from datetime import datetime
from sqlmodel import Field, SQLModel  

#entidad session
class User_session(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="user.id")
    date_inicio : datetime =Field(default_factory= datetime.now)
    date_fin : datetime = Field(default_factory= datetime.now)
