from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

 # request
class SessionCreate_Request(BaseModel):
    """
    Schema para la creacin de una sesion de un usuario \n
    args: \n 
          1. name (str) valor not null, \n
          2. minimo 4 caracteres, maximo 50 caracteres\n
    args: \n 
          1. password (str) valor not null,\n
          2. minimo 8 caracteres \n
          3. debe contener caracteres especiales\n
    """
    name: str = Field(..., min_length=4, max_length=50)
    password: str = Field(..., min_length=8, regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')                  

# response

class SessionCreate_Response(BaseModel):
    """
    Schema para la respuesta de la creacion de una sesion de un usuario \n
    args: \n 
          1. status (int) valor not null,\n
          2. message (str) mensaje de respuesta,\n
          3. usuario_id (int) id del usuario registrado,\n
    """
    status: int = Field(..., ge=200, le=299)
    message: str = Field(..., min_length=4, max_length=50)
    usuario_id: int = Field(..., ge=1)