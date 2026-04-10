from sqlmodel import Session, select
from app.baseconfig import engine
from app.session.schema import SessionCreate_Request
from app.register.model import User

def autenticate_user(data: SessionCreate_Request):
    with Session(engine) as session:
        statement = select(User)
        results = session.exec(statement)
        for user in results:
            #m validacion de usuario , devolver true si existe el usuario y false si no existe
            if data.password == user.password:
                return True
            else:
                return False

def get_user_by_username(data: SessionCreate_Request):
    with Session(engine) as session:
        statement = select(User).where(User.name==data.name)
        user = session.exec(statement).first()
        print(user)
        return user