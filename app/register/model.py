from sqlmodel import Field, SQLModel 
from pydantic import field_validator

#entidad usuario
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str =Field(min_length=4, max_length=50)
    password: str =Field(min_length=8)
