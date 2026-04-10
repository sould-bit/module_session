from app.session.use_case import login
from app.session.schema import SessionCreate_Request , SessionCreate_Response
from fastapi import APIRouter

router = APIRouter()

@router.post("/login", response_model=SessionCreate_Response)
def login_endpoint(data: SessionCreate_Request):
    """
    funcion para iniciar sesion
    """
    return login(data)



