class: center, middle, inverse, layout
# Módulos en Python
## Programación I

---

class: inverse
layout: true

---

# Módulos

<cite>
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.
</cite>




---
 
# Importar un módulo

## Opción 1

Importar el módulo completo, las funciones se referencian con el nombre del módulo 

```python
import math

print(math.sqrt(2))
print(math.pow(2, 3))
```


```python
import turtle

turtle.forward(100)
```

---

# Importar un módulo

## Opción 2

Importar **sólo algunas funciones** del módulo completo. Las funciones se referencian sólo por su nombre 

```python
from math import sqrt, pow

print(sqrt(2))
print(pow(2, 3))
```


```python
from turtle import forward, left, right

turtle.forward(100)
```

---

# Importar un módulo

Cuando importamos un módulo, todas las sentencias (statements) dentro de el se ejecutan. Las declaraciones (por ejemplo las funciones) no, ya que no son órdenes.

¿Cómo podemos evitar esto?

```python
if __name__ == '__main__':
    dibujar_personaje()
```

El interprete define una variable llamada *__name__* con el nombre del módulo. Esa condición nos permite saber si estamos ejecutando el archivo desde el intérprete. La condición da falso si el archivo está siendo importado desde otro.


---

# Algunos módulos de la biblioteca de Python

* **math**: funciones matemáticas
* **os**:   funciones del sistema operativo
* **datetime**: funciones para trabajar con fecha y hora
* **random**: crear números aleatorios

Índice de módulos estándar: [https://docs.python.org/3/py-modindex.html](https://docs.python.org/3/py-modindex.html)

---

# Ejercicio

Crear una escena importando y utilizando [los personajes creados por sus compañeros](https://drive.google.com/drive/u/2/folders/1ziZ1ClFpQ0JKwSYS5iFeaF80oQXblRPf):

* Debe importar y utilizar como mínimo 3 personajes (pueden importar el suyo)
* Debe agregar algún detalle adicional a la escena (piso, árbol, sol, nubes, etc.)

### Tips

* Deben abrir el archivo que desean importar y ver qué funciones exporta
* Pueden agrandar la pantalla con:
```python
turtle.screensize(1200, 1000)
```
* Pueden mover a la tortuga con:
```python
turtle.penup()
turtle.goto(100, 100)
```