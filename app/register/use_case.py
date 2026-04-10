from app.register.schemas import UserRegister_Request, UserRegister_Response
from app.register.repository import save_user
from app.register.repository import get_user_by_username
from app.register.model import User


#RECIVIMMOS LA VALIDACION DE PYDANTIC  "CONTRATO DE ENTRADA QUE NESESITA PARA REGISTRAR UN USUARIO "
def register_user(data: UserRegister_Request):
    """
    mfuncion para registrar usuario
    """

    #validamos que el usuario no exista
    user = get_user_by_username(data)
    if user:
        return UserRegister_Response(
            status=400,
            message="Usuario ya existe",
            usuario_id=user.id
            
        )

    #por temas de tiempo por ahjora no guardamos el hash de la contraseña , si no la contraseña en si misma 
    user = User(
        name=data.name,
        password=data.password
    )

    #guardar usuario en la base de datos
    save_user(user)
    print("usuario guardado exitosamente")
    
    #retornar respuesta
    return UserRegister_Response(
        status=200,
        message="Usuario registrado exitosamente",
        usuario_id=user.id        
    )
