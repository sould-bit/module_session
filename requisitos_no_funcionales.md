> GLOSARIO

----
- ``SALT`` : valor aleatorio que se asigna a un usuario antes de el hash   
    - previene  *rainbow table* asi el atanacte debera recalcular un *rainbow table* para cada salt
    - al tener un salt por  usuario evitamos que dos usuarios con la misma contraseña tengan el mismo hash
---

# Seguridad

1. las contraseñas deben ser manejadas con **hash** + **salt**

# Consistencia
1.  el usuario debe ser unico en la base de datos 
2. transacciones atomicas " si falla el registro no se guarda nada parcial"

# Manejo de errores

1. mensajes genericos que no revelen datos sencibles mni detalles internos del sistema 