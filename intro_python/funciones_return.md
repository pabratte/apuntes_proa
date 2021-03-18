class: center, middle, inverse, layout
# Funciones en Python
## Programación I

---

class: inverse
layout: true

---

## Repaso Funciones

* Las funciones son porciones de código que separamos e identificamos con un nombre:
	- Permiten organizar mejor el programa
	- Evitan repetir código
	- Facilitan la reutilización
	- Facilitan compartir código y trabar en equipo 
	- ...

---
## Repaso Funciones

Las funciones se definen con:
* Palabra reservada *def*
* El nombre debería ser un verbo que de idea de la acción que realiza
* Los parámetros van declarados entre paréntesis ()
* : para indicar que es un bloque
* Las instrucciones van debajo indentadas para indicar que forman parte de la función

```
def sumar(valor1, valor2):
	resultado = valor1 + valor2
	print("La suma es: {}".format(resultado))

sumar(1, 2)
```

---

## Parámetros

Son los datos que necesita la funcion para operar

```
def sumar(valor1, valor2):
	resultado = valor1 + valor2
	print("La suma es: {}".format(resultado))

sumar(1, 2)
```


* **Parametros formales**: (o sólo parámetros) el nombre con el que lo declaro, el que voy a usar **dentro de la función** para referirme al valor. Es un valor que **todavía no conozco** pero que el usuario me va a especificar cuando llame a la función.

* **Parametros actuales**: (o argumentos) es el **valor concreto** que el usuario especifica para un parámetro formal al invocar a la función.

En el ejemplo:
* *valor1* y *valor2* son *parámetros formales*
* *1* y *2* son los *parámetros actuales*

---

## Parámetros

Cuando **definimos** una función usamos **parámetros formales** (no sabemos el valor todavía, pero necesitamos ponerle un nombre a esa información que el usuario va a pasar).

Cuando **invocamos** la función le pasamos **parámetros actuales** (o argumentos) que son los valores concretos con los que la función va a trabajar.

---

## Retorno de valores

* ¿Qué pasa si la función tiene que devolver datos?
* ¿Cómo devuelve la función el resultado al programa que la invocó?
* ¿Sirve esta función si yo no quiero mostrar el valor de la suma sino utilizarlo para otro cálculo?
* ¿Sirve si el programa que utiliza la función requiere mensajes en inglés?

```
def sumar(valor1, valor2):
	resultado = valor1 + valor2
	print("La suma es: {}".format(resultado))

sumar(1, 2)
```
---

## Retorno de valores

* La palabra reservada *return* permite indicar el valor que **devuelve** la función al programa
* Devolver un valor permite *"evaluar"* la función como si se tratara de una variable.

```
def sumar(valor1, valor2):
	resultado = valor1 + valor2
	return resultado

r = sumar(1, 2)
print("La suma es: {}".format(r))
```

De esta forma:
* la función es **más reutilizable** porque no está atada a mensajes de entrada/salida (me devuelve el valor y yo hago lo que quiero).
* las responsabilidades quedan mejor definidas (y el programa mejor diseñado)
	- La función se encarga de hacer el cálculo, no de formatear la salida
	- El programa principal (main) se encarga de formatear la salida, no de realizar el cálculo

---

## Devolver más de un valor

Las funciones pueden devolver más de un valor si son *"empaquetados"* en una única estructura. 

### Usando tuplas
```
def sumar_y_restar(valor1, valor2):
	suma = valor1 + valor2
	resta = valor1 - valor2
	return (valor1, valor2)

(r1, r2) = sumar_y_restar(1, 2)
print("La suma es: {}".format(r1))
print("La resta es: {}".format(r1))
```

*Las tuplas se pueden asignar como variables comunes*. En este caso la suma se almacenará en *r1* y la resta en *r2*.
---

## Devolver más de un valor

### Mediante diccionario

```
def sumar_y_restar(valor1, valor2):
	resultado = {
		'suma': valor1 + valor2,
		'resta': valor1 - valor2,
	}
	return resultado

r = sumar_y_restar(1, 2)
print("La suma es: {}".format(r['suma']))
print("La resta es: {}".format(r['resta']))
```

Utilizar tuplas o diccionarios depende de si son pocos o son muchos los valores que necesito devolver. Si sin pocos me conviene la tupla (acceso por posición) si son muchos (o quiero acceder a los campos por nombre) quizás convenga el diccionario.

---

## Variables locales vs variable globales

**Variable Local**: sólo puede ser accedida dentro de la función en la cual fue declarada. No es accesible desde otros ámbitos.

**Variable Global**: declaradas fuera de las funciones, se pueden acceder desde cualquier lugar del programa (son una mala práctica, no ayudan a organizar el código, pero a veces no se pueden evitar)

```
def sumar(valor1, valor2):
	resultado = valor1 + valor2

sumar(1, 2)
print("La suma es: {}".format(resultado))
```

El pasaje de parámetros y el retorno de valores son para evitar tener variables globales y disponer un mecanismo de comunicación entre la función y el exterior.

---

## Pasaje de parámetros por valor vs por referencia

¿Cuál es la salida del siguiente programa?

```
def prueba(valor):
	valor = valor + 1

v = 1
prueba(v)
print(v)
```

---

## Pasaje de parámetros por valor vs por referencia

¿Cuál es la salida del siguiente programa?

```
def prueba2(l):
	l.append(4)
	l.append(5)
	l.append(6)

l = [1, 2, 3]
prueba2(l)
print(l)
```

---

## Pasaje de parámetros por valor (o por copia)

El parámetro formal se crea como una **variable nueva** que guarda **una copia** del valor del parámetro formal.

Si modificamos el parámetro, lo que estamos modificando es la copia (variable local) que hay en la función. Cuando se sale de la función es como si "no hubiera pasado nada". 

```
def prueba(valor):
	valor = valor + 1

v = 1
prueba(v)
print(v)
```

---

## Pasaje de parámetros por referencia

El parámetro formal es un *alias* (otro nombre) para la misma variable del parámetro formal.

**No se genera una copia de la variable.**

Si modificamos el parámetro, al salir de la variable original queda modificada. 

```
def prueba2(l):
	l.append(4)
	l.append(5)
	l.append(6)

l = [1, 2, 3]
prueba2(l)
print(l)
```

---

## Pasaje de parámetros por referencia vs por valor

<center>
<video preload="auto" poster="https://img-9gag-fun.9cache.com/photo/az9pOnp_460s.jpg" style="min-height: 269.953px; width: 500px;" loop="" width="500" autoplay>
<source src="az9pOnp_460svvp9.webm" type="video/webm; codecs=&quot;vp9, opus&quot;">
<source src="az9pOnp_460sv.mp4" type="video/mp4">
</video>
</center>
---

## Pasaje de parámetros por referencia vs por valor

### ¿Cuándo se hace uno y cuándo el otro?

Lo maneja el lenguaje:
- Tipos primitivos (int, float) => por valor
- Tipos complejos (string, list, dict) => por referencia

### ¿Por qué?

Porque los tipos complejos pueden ser arbitrariamente grandes y sería ineficiente generar copias.

¿Qué pasaría si trato de pasar por copia un arreglo de 1000000000 elementos?


---

# Ejercicio

Un comercio de partes para PCs gamer necesita actualizar su lista de precios de acuerdo con la última subida del dólar. 
El sistema almacena los productos en una lista en donde cada producto es un diccionario que contiene los siguientes campos:
```
[
	{
		id: 1,
		nombre: 'Disco Solido SSD - 240GB - GIGABYTE',
		precio: 3696,
	},
    {
		id: 2,
		nombre: 'Mouse GAMER LOGITECH G300S GAMING',
		precio: 2904,
	},
]
```
---

# Ejercicio

1. Cargar la lista de productos desde la "base de datos" utilizando la función cargar_productos(), del módulo db_productos.
2. Definir una función *mostrar_productos()* que reciba la lista de productos, no retorne nada, y muestre la lista con el siguiente formato:
	```
	Producto: {id}
	{nombre} ${precio}
	
	Producto: {id}
	{nombre} ${precio}
	```
3. Definir una función *calcular_precio_actualizado()* que reciba: el **precio anterior** y **porcentaje de aumento** y retorne: **el precio con el aumento**.

4. Crear una función *actualizar_precios()* que reciba **la lista de productos** y **el porcentaje de aumento**. La función debe recorrer cada producto de la lista e invocar *calcular_precio_actualizado()* (a la cual tendrá que pasarle el precio del producto y el porcentaje de aumento) para obtener el precio actualizado y modifique la lista "in-place" actualizando el precio de cada producto. La función no debe retornar nada sino dejar modificada la lista pasada por el usuario.

---

# Ejercicio

5- Desde el programa principal:
* Mostrar la lista de precios cargada utilizando la función mostrar_productos()
* Solicitar al usuario que ingrese el porcentaje de aumento
* Aplicar el aumento a los precios de la lista con la función actualizar_precios()
* Mostrar por pantalla la lista de precios actualizada utilizando la función mostrar_productos()

6- **Grabar un screencast** explicando las funciones que crearon (que reciben, qué devuelve, qué hacen) y cómo aplicaron funciones para la resolución del ejercicio.

Pueden trabajar en grupos de hasta 3 personas con condición de que **todos expliquen algo** en el screencast




