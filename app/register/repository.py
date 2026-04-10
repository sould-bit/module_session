from sqlmodel import Session, select
from app.baseconfig import engine
from app.register.schemas import UserRegister_Request
from app.register.model import User


# guardamos el usuario en la base de datos
#creamos una Session para guardar el usuario (Session(engine))
def save_user(data: UserRegister_Request):
    with Session(engine) as session:
        session.add(data)
        session.commit()
        session.refresh(data)
        return data

#realizammos una consulta 
#abrimos session  seleccionamos el modelo user , donde los valores del contrato de entrada sea igual a los datos proporcionados por el cliente 
def get_user_by_username(data: UserRegister_Request):
    with Session(engine) as session:
        statement = select(User).where(User.name==data.name)
        user = session.exec(statement).first()
        return user