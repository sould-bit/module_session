# ACTORES GLOBALES
- sistema 
    - API
    - Backend
    - Frontend
- cliente

**UC-01**
>El usuario debe poder registrarse 

**precondiciones**

- el usuario debe encontrarse en la pantalla loguin y haber selecionado registra cuenta 

flujo  principal **(REGISTRARSE)**

A [usuario] --> ingresa datos **(name, constraseña)**

B [sistema] --> valida datos codigos **[ 200 ok ]**

C [sistema] -->  crea usuario

D [sistema] --> mensaje **Registro exitoso**


FLUJOS ALTERNATIVOS 

B [sistema] --> vaida datos

    |  el usuario ya existe  --> sistema muestra error   [409 : conflic] 
B [sistema] --> valida datos
    
    | contraseña no cumple requisitos --> sistema muestra error [400 : bad request]


**INPUTS**

`
nombre : str (max 50 caract)
`

`
password : str (min 8 caract)` 


**OUTPUT**

exito `201 created`
- objeto con perfil creado sin contraseña **mensaje registro exitoso**

error `401/409`
- `409 conflict` usuario  registrado
- `400 bad request` datos invalidos 



**UC-02**
> el usuario debe poder iniciar seccion 

**precondiciones**
- usuario debe haberse registrado


flujo  principal **(INICIAR SECCION)**

A [usuario] -->  ingresa datos **(name, constraseña)**

B [sistema] -->  valida datos codigos **[ 200 ok ]**

C [sistema] -->  iniciar seccion 

D [sistema] -->  mensaje **autenticacion exitosa**


FLUJOS ALTERNATIVOS 

B [sistema] --> vaida datos

    |  usuario no registrado  --> sistema muestra error   [409 : conflic] 

B [sistema] --> vaida datos
    
    | contraseña incorrecta --> sistema muestra error [401 : unautorized]



**INPUTS**

`
nombre : str (max 50 caract)
`

`
password : str (min 8 caract)` 


**OUTPUT**

exito `200 susccefull`
- inicio exitoso **mensaje** autentificacion satisfactoria 

error `401/409`
- `409  conflict` usuario no registrado 
- `401 unautorized` contraeña no coincide


[back to readmi](readmi.md)