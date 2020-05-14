class: center, middle, inverse, layout
# Estructuras de datos en Python
## Programación I

---

class: inverse
layout: true

---

# Estructuras de datos en Python

* Lista
* Diccionario
* Tupla
* Conjunto (set)


---
 
# Lista

* Colección **ordenada** de elementos. Generalmente del mismo tipo.
* Los elementos son accedidos en base a su **posición** dentro de la lista.
* Ejemplo: una lista de compras


---

# Lista

## ¿Qué se puede hacer con una lista?

* Acceder a un elemento especificando su posición
* Recorrer todos sus elementos
* Conocer la cantidad de elementos dentro de la lista
* Agregar un elemento al final (append)
* Insertar un elemento en una posición cualquiera
* Eliminar un elemento
* Buscar si un elemento está dentro de la lista
* ...

---

# Lista

## Inicializar

```python
# crea una lista vacía (sin elementos)
l1 = []

# crea una lista con 3 elementos de tipo string
l2 = [“manzanas”, “bananas”, “naranjas”]
```

---


# Lista

## Acceder a un elemento dado su posición

```python
l2 = [“manzanas”, “bananas”, “naranjas”]

# muestra “manzanas”
print( l2[0] )

# muestra “bananas”
print( l2[1] )
```

* Para acceder a un elemento de la lista se utilizan [ ] *(pero ojo! no confundir con la inicialización)*
* Las posiciones empiezan desde 0 (cero)

---

# Lista

## Recorrer todos los elementos de una lista

```python
l2 = [“manzanas”, “bananas”, “naranjas”]

for elem in l2:
  print(elem)
```

* Léase: para cada elemento (llamémosle *elem*) dentro de la lista... imprimir *elem*

---

# Lista

## Recorrer todos los elementos de una lista mediante un contador

```python
l2 = [“manzanas”, “bananas”, “naranjas”]

for cont in range(len(l2)):
  print( l2[i] )
```

* *len(l2)* devuelve un entero con la cantidad de elementos dentro de la lista *l2*
* El bucle *for* hace que la variable *cont* vaya tomando todos los valores entre 0 y len(l2)-1
* En una lista de **N** elementos la primera posición siempre es **0** y la última posición **N-1**
* Dentro del for se accede a cada elemento de la lista con mediante su índice
* A diferencia de la anterior, esta forma nos permite modificar los elementos de la lista

---

# Lista

## Ejemplo 

Se tiene una lista de precios de los distintos elementos del kiosco de la escuela. Debido a la devaluación
se debe aplicar un recargo de $100 a cada uno de los elementos. Escriba un programa que recorra la lista y aplique
el recargo a los precios de la misma. Luego muestre la lista.


```python
precios = [500, 450.5, 849, 721]

# recorrer la lista y modificar los precios
for i in range(len(precios)):
  precios[i] = precios[i] + 100

# mostrar la lista
for p in precios:
  print(p)
```

---
# Lista

## Agregar un elemento al final (append)

*append()* recibe entre paréntesis un valor y lo agrega al final de la lista

```python
compras = []

compras.append("manzanas")
compras.append("bananas")
compras.append("naranjas")

for elem in compras:
  print(elem)
# muestra:
#
# manzanas
# bananas
# naranjas
```
---

# Lista

## Insertar un elemento en una posición cualquiera

*insert()* recibe entre paréntesis y separadas por comas:
* el valor a insertar
* la posición en donde insertarlo

```python
compras = []

compras.append("manzanas")
compras.append("bananas")
compras.append("naranjas")

# inserta "peras" en la pos 1 (donde estaba "bananas")
# bananas se desplaza hacia adelante
compras.insert("peras", 1)

for elem in compras:
  print(elem)
# muestra:
# manzanas
# peras
# bananas
# naranjas
```

---
# Lista

## Eliminar un elemento

*remove()* recibe el valor del elemento a quitar

```python
compras = [ "manzanas", "peras", "bananas", "naranjas" ]

compras.remove("bananas")

for elem in compras:
  print(elem)
# muestra:
#
# manzanas
# peras
# naranjas
```
* Si el elemento se encuentra repetido **sólo se eliminará el primero**

---

# Lista

## Ejercicio #1

La siguiente lista exhibe los platillos favoritos del profe. Completá el siguiente código para agregar al final de la lista 2 o 3 comidas que te gusten. Luego probá que el código muestre correctamente la lista completa. 

```python
comidas = [ "pizza", "lomitos", "milanesas" ]

# COMPLETAR: agregue sus comidas favoritas al final de la lista

for c in comidas:
  print(c)
```
---

# Lista

## Ejercicio #2

El centro de estudiantes de ProA Técnica está llevando adelante un proyecto de reciclado de botellas. Varios alumnos salieron a recolectar y en el siguiente código la lista *cant_botellas* posee la cantidad de botellas que juntaron 5 estudiantes. Completar el código para recorrer la lista y obtener la cantidad total de botellas que juntaron entre todos.

```python
cant_botellas = [ 5, 1, 0, 7, 20 ]

total_botellas = 0

# COMPLETAR: recorrer la lista y obtener la suma de todas
# botellas juntadas por todos los estudiantes

print("El total de botellas juntadas es {}".format(total_botellas))
```

---

# Lista

## Ejercicio #3

Escriba un programa en Python que cree una lista vacía y le agregue 10 valores enteros ingresados por el usuario. Luego, el programa debe mostrar la lista. Finalmente el programa debe recorrer la lista y mostrar la cantidad de valores ingresados que resultaron mayores a 100.



