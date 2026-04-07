# ENTIDADES


|ENTIDAD |ATRIBUTO|TYPE|
|--------|--------|-    |
|usuario|id      |fk (int)|
|       |name    |str  |
|       |password| str |




*validaciones de datos*

`name` :

1. el sistema debe validar si el name ya existe , ya que es el atributo relacional , FK de la entidad **usuarios**

`password` :

1. el sistema debe validar que el password cumpla con los requisitos  **caracteres especiales**

|ENTIDAD |ATRIBUTO|TYPE|
|--------|--------|-    |
|SESSION | usuario_id|int|
|        |date_inicio    |datetime |
|        |date_fin    |datetime |






# REGLAS
**USUARIOS**
```` 
1. no puede existir usuarios duplicados
2. la contraseña puede tener minimo 4 caracteres
3. la constraseña debe tener caracteres especiales 
````
**SESSION**
````
1. un usuario no puede iniciar seccion sin antes registrarse 
````

[back to readmi](README.md)