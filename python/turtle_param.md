class: center, middle, inverse, layout
# Arte generativo con Python
## Programación I

---

class: inverse
layout: true

---

## Arte generativo

Arte que, parcialmente o en su totalidad, ha sido creado con el uso de un sistema autónomo. 

A menudo se refiere al arte algorítmico (obras de arte generadas por computadora mediante algoritmos).

Algunos dicen que:
<br>
<cite>
Es un diálogo entre el artista y la computadora.
</cite>


<img width="30%" src="https://miro.medium.com/max/3200/1*Dx-XX2mn5Xeb9YLiH_4rPg.png">

<a href="https://www.google.com/search?tbm=isch&q=generative+art" target="_blank">Ejemplos</a>

---

## Funciones con parámetros en Python

**Definir** una función con parametros:

```
def cuadrado(x, y, tam):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    # dibujar el cuadrado
    for i in range(4):
        turtle.forward(tam)
        turtle.left(90)
```
La función tiene 3 parámetros (como "slots") para recibir información (x, y, y tam) sobre la posición y tamaño del cuadrado que se va a dibujar.

---


## Funciones con parámetros en Python

**Usar** una función con parámetros:

Definir una función con parametros:

```
cuadrado(100, 200, 20)
cuadrado(200, 100, 10)
xx = 0
yy = -100
cuadrado(xx, yy, 30)
```
* Al llamar a la función, se pasan los valores específicos para los parámetros, **en orden** por ejemplo (100 para x, 200 para y, 30 para tam)
* Se pueden utilizar variables
* Dentro de la función, nos referimos a estos valores con los nombres de los parámetros que declaramos (x, y, tam)
* En Python, también se puede pasar parámetros por nombre sin respetar el orden, por ejemplo:
```
cuadrado(tam=20, y=100, x=200)
```
---

## Ejemplo caracol

.left-column50[
```
import utils

# valores iniciales
angulo = 0
tam = 10
steps = 15
blue = 0
y = 0
x = 0

for i in range(steps):
    utils.cuadrado(x, y, angulo, tam, (1, 0, blue))
    tam = tam + 5
    angulo = angulo + 360.0/steps
    blue = blue + 1/steps
    #y = y - 5
    #x = x + 2

utils.guardar_imagen("caracol")
```
]

.right-column50[
<div style="text-align: center;">
<img src="caracol_captura.png">
</div>
]
---

## Numeros aleatorios en Python

Módulo random

```
import random

# obtiene un float aleatorio entre [0, 1]
f = random.random()

# obtiene un entero aleatorio entre [-100, 200]
i = random.randint(-100, 200)
```

---

## Ejemplo cuadrados

.left-column50[
```
import utils
import random

for i in range(500):
    x = random.randint(-200, 200)
    y = random.randint(-400, 400)
    ang = random.randint(0, 360)
    tam = random.randint(10, 50)
    color = 	(
    		random.random(), 
    		random.random(),
    		random.random()
    		)
    utils.cuadrado(x, y, ang, tam, color)

utils.guardar_imagen("cuadrados")
```
]

.right-column50[
<br>
<div style="text-align: center;">
<img src="cuadrados.png" width="90%">
</div>
]

---

## Ejemplo flores

<div style="text-align: center;">
<img src="flores_captura.png" width="80%">
</div>

---

# Archivos de los ejemplos

* <a href="utils.py" target="_blank">utils.py</a>
* <a href="caracol.py" target="_blank">caracol.py</a>
* <a href="cuadrados.py" target="_blank">cuadrados.py</a>
* <a href="turtle_flower_param.py" target="_blank">turtle_flower_param.py</a>

---

# Actividades

1. Imaginar 2 o 3 formas simples
2. **Crear 2 funciones** que dibujen esas formas (una forma por función) y **reciban al menos 5 parámetros** (posición, angulo, color, etc)
3. Crear una imagen de arte generatov invocando varias veces a las funciones alterando los valores de los parámetros
4. Subir el código a la tarea en el aula virtual
5. Subir la captura de nuestra obra maestra al grupo de WhatsApp


* Tip: antes comenzar a dibujar dentro de la función, conviene reiniciar el estado de la tortuga (posición, ángulo, color, etc) como en el ejemplo del cuadrado en <a href="utils.py" target="_blank">utils.py</a>
* Tip: pueden utilizar la función *guardar_imagen()* en <a href="utils.py" target="_blank">utils.py</a> para guardar una captura en formato PNG

---
