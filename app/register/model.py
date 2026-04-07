from sqlmodel import Field, SQLModel  

#entidad usuario
class User(SQLModel, table=True):
    id: int = Field(autoincrement=True, primary_key=True)
    name: str =Field(min_length=4, max_length=50)
    password: str =Field(min_length=8, regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

