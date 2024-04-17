# Tarea 2.3
## 1.- Expresión regular que valide un password fuerte:
* 1 minúscula
* 1 mayúscula
* 1 numero
* 1 carácter especial
* 8 caracteres de longitud
### Expresión regular:
~~~
^(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[@#$%/&*+-_!¡¿?]).{8}$
~~~
## 2.- Expresión Regular que valide un Nombre de usuario
* Longitud de 3 a 16 caracteres
* Letra o numero o guion medio o bajo
### Expresión regular:
~~~
^[\w*-]{3,16}$
~~~
