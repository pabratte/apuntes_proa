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


---

# Diccionario

* Colección de pares **clave -> valor**.
* No hay un orden entre los elementos (no se puede establecer/no es importante).
* La clave siempre es de tipo string.
* El valor puede ser de cualquier tipo.
* Los elementos son accedidos en base a su **nombre de clave**.
* Ejemplo: un diccionario.

---

# Diccionario


.left-column50[

## Ejemplo

```python
player1 = {
  "name": "Sylvan",
  "level": 1,
  "attack": 160,
  "max-hp": 600,
}


# mostrar poder de ataque de player 1
print(player1["attack"])
```
]

.right-column50[
<div style="text-align:center;">
<img src="img/Arc.jpg" style="width: 90%;">
</div>
]

---

# Lista vs Diccionario

.left-column50[

## Lista
* Orden secuencial de los elementos
* Generalmente se recorre toda la lista elemento por elemento
* Los valores se acceden por su **posición** 
* Los valores, generalmente, son del **mismo tipo**


*Pensar el uso de la lista como una **novela**: se debe leer capítulo por capítulo en orden*
]

.right-column50[
## Diccionario
* No importa el orden
* Se busca un elemento particular conociendo su clave
* Los valores se acceden por su **nombre de clave**
* Los valores, generalmente, son de **tipos distintos**

*Pensar el uso del diccionario como un **diccionario**: no se lee todo, sólo se busca una palabra*
]

---

# Diccionario

## ¿Qué se puede hacer con un diccionario?

* Inicializar/crear
* Acceder a un elemento especificando su clave
* Conocer si un valor clave está presente en el diccionario
* Agregar/modificar un elemento especificando su clave y valor


---

# Diccionario

## Inicializar

```python
player1 = {
  "name": "Sylvan",
  "level": 1,
  "attack": 160,
  "max-hp": 600,
}

edades = {"Santiago": 17, "Mercedes": 14, "Lautaro": 14}
```

---

# Diccionario

## Acceder a un elemento dada su clave

Se accede al *valor* de un elemento especificando entre corchetes [] su *clave*

```python
edades = {"Santiago": 17, "Mercedes": 14, "Lautaro": 14}

print(edades["Mercedes"])


print(edades["Juan"]) # explota todo

```

* Si la clave no existe el interprete lanza un **KeyError**
* **¡OJO!** la clave **siempre debe ser un string**
* **¡OJO!** las claves son **case-sensitive** (distinguen mayúsculas y minúsculas)

---

# Diccionarios

## Saber si un elemento existe dentro de un diccionario

Se puede utilizar el operador **in**

```python
edades = {"Santiago": 17, "Mercedes": 14, "Lautaro": 14}

nombre = input()

if nombre in edades:
  print(edades[nombre])
else:
  print("{} no se encuentra en el diccionario".format(nombre))
```

---


# Diccionarios

## Agregar/modificar un elemento especificando su clave y valor


```python
player1 = {
  "name": "Sylvan",
  "level": 1,
  "attack": 160,
  "max-hp": 600,
}

# si la clave existe, se modifica su valor
player1["attack"] = 200

# si la clave no existe, se agrega
player1["speed"] = 100

print(player1)
```

---

# Diccionarios

## Ejercicio #1

Elija un dispositivo tecnológico, por ejemplo, su celular, PC, Smart-TV, etc. Utilice un diccionario para representarlo proponiendo los atributos (claves) que usted considere. Tenga en cuenta lo siguiente:
* Debería tener al menos 3 claves
* Debería utilizar al menos 2 tipos de datos distintos para sus valores


---

# Diccionarios

## Ejercicio #2

Teniendo en cuenta el siguiente diccionario:

```python
alumno1 = {
  "nombre": "Sandra",
  "edad": 15,
}
```

Escriba un programa que permita crear otro diccionario, con la misma estructura, con datos ingresados por el usuario. Luego el programa debe mostrar el nombre del alumno cuya edad es mayor.

---

# Diccionarios

## Ejercicio #3

Un número racional (numerador y denominador) se puede representar mediante un diccionario. Por ejemplo, el siguiente diccionario se utiliza para representar el racional con numerador = 1 y denominador = 2:
```python
racional1 = {
  "num": 1,
  "den": 2,
}

```

Escriba un programa que permita al usuario ingresar 2 valores **racionales (numerador y denominador)** y los **almacene en diccionarios**. Luego el programa debe **calcular y mostrar la multiplicación** de las 2 fracciones.

---

# Diccionarios

## Ejercicio #3

Recordar que, para multiplicar dos racionales, el numerador se multiplica con el numerador y el denominador con el denominador, es decir:
<div style="text-align: center;">
<img src="img/hqdefault.jpg" style="width: 50%;">
</div>
en código:
```python
resultado["num"] = racional1["num"] * racional2["num"]
resultado["den"] = racional1["den"] * racional2["den"]
```
