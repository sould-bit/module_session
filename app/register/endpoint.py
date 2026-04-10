from app.register.use_case import register_user
from app.register.schemas import UserRegister_Request , UserRegister_Response
from fastapi import APIRouter

router = APIRouter()


@router.post("/register", response_model=UserRegister_Response)
def register(data: UserRegister_Request):

    #llamammos al caso de uso 
    return register_user(data)