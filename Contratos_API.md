# ENDPOINT

*MODULO SESSION*

- **A**

   `POST /API/V1/register`
- **B**  
    ` GET /API/V1/loguin`


# PYLOAD *(REQUEST)*

**A**  `POST /API/V1/register`
``` json
{
    "name": "juanito23",
    "password": "jainit*05"
}
```

**B** ` GET /API/V1/loguin`

``` json
{
    "name": "juanito23",
    "password": "jainit*05"
}
```

# RESPONSES


**A** `POST /API/V1/register`
``` json
{
    "satus": 201,
    "message": "registro exitoso",
    "usuario_id": 1
}
```

**B** ` GET /API/V1/loguin`

``` json
{
    "status": 200,
    "message": "autentificacion exitosa",
    "usuario_id": 1
}
```


# ERRORES

**A** `POST /API/V1/register`
``` json
{
    "satus": 409,
    "error": "el usuario ya existe",
}
```

**A** `POST /API/V1/register`
``` json
{
    "satus": 400,
    "error": "datos invalidos",
}
````

**B** ` GET /API/V1/loguin`
``` json
{
    "satus": 409,
    "error": "el usuario no se encuentra registrado",
}

````
**B** ` GET /API/V1/loguin`
``` json
{
    "satus": 401,
    "error": "la contraseña no coincide",
}
````


 [bamck to README](README.md)