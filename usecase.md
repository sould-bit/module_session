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


**INPUTS**

`
nombre : str (max 50 caract)
`

`
password : str (min 20 caract)` 


**OUTPUT**

exito `201 created`
- objeto con perfil creado sin contraseña **mensaje registro exitoso**

error `401/409`
- `409 conflict` usuario  registrado



**UC-02**
> el usuario debe poder iniciar seccion 

**precondiciones**
- usuario debe haberse registrado

**INPUTS**

`
nombre : str (max 50 caract)
`

`
password : str (min 20 caract)` 


**OUTPUT**

exito `200 susccefull`
- inicio exitoso **mensaje** autentificacion satisfactoria 

error `400/409`
- `409  conflict` usuario no registrado 
- `401 unautorized` contraeña no coincide


[back to readmi](readmi.md)