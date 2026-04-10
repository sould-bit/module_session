from app.session.schema import SessionCreate_Request, SessionCreate_Response
from app.session.repository import autenticate_user, get_user_by_username

def login(data: SessionCreate_Request):
    
    user = get_user_by_username(data)
    
    if not user:
        return SessionCreate_Response(
            status=404,
            message="Usuario no encontrado",
            usuario_id=None
        )
    
    validation = autenticate_user(data)
    print(validation)
    if not validation:
        return SessionCreate_Response(
            status=401,
            message="error en la autenticación contraseña invalida",
            usuario_id=None
        )
    return SessionCreate_Response(
        status=200,
        message="Usuario autenticado exitosamente",
        usuario_id=user.id
    )

