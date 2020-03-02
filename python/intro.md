

##??? Lenguajes compilados vs interpretados


Ejemplo de programa con errores

##??? Uso interactivo...



## Variables

En programación, el término **variable** describe un espacio en la memoria donde se guarda información (números, texto, etc). Otra forma de pensar a la variable es como una *etiqueta* para determinada información. Por ejemplo, la en el código que sigue la variable *vidas* guarda el numero 3, que puede indicar la cantidad de vidas restantes en un videojuego. 

```
vidas = 3
```

## Nombres de variables

A la hora de elegir un nombre para una variable se debe respetar una serie de reglas que son generalmente las mismas en la mayoría de los lenguajes:

* Debe comenzar con una letra
* No debe contener espacios
* Sólo debe contener letras, números y guiones bajos (_), no se pueden utilizar caracteres "raros" como %$#-, letras con acento, etc.
* Son *case-sensitive*, es decir sensibles al uso de mayúsculas y minúsculas. Por lo cual los siguientes son tres nombres distintos: ```nivel```, ```Nivel```, ```NIVEL```

Además, elegir un buen nombre para una variable es importante para que a medida que el código se vuelva más complejo sea sencillo de comprender, por nosotros mismos o por otros.

Algunas recomendaciones a la hora de elegir nombres para una variable son:

* Utilizar un sustantivo que describa **qué** es lo que almacena esa variable.
* Que la primer letra sea minúscula (los nombres que empiezan con mayúscula generalmente se reservan para clases).
* Si el nombre elegido para la variable tiene varias palabras se puede utilizar camelCase o separar por guiones bajos. Por ejemplo: ```intentosFallidos``` o ```intentos_fallidos```.


## Variables vs constantes

Las **constantes** son valores que se mantienen siempre igual durante toda la ejecución del programa. Son constantes, por ejemplo, los valores:

* ```3```
* ```4.85```
* ```"Hola usuario"```
* ```True```

Estos valores generalmente tienen relación con la lógica del problema.


## Tipos de datos

Cada dato que forma parte de un programa, tanto las variables como las constantes, **tienen un tipo asociado** (entero, real, cadena de texto, etc).

Algunos de los tipos de datos principales en python son

* int
* float
* str (string)
* bool

Debajo se muestran ejemplos de variables para cada uno de estos tipos.

```
i = 3
f = 7.1
s = "hola"
b = True
```

**El tipo de un dato es importante porque indica qué operaciones se pueden hacer con el mismo**. Por ejemplo, se puede sumar números enteros o reales, pero no se puede sumar cadenas de texto o valores de verdad (booleanos).

En Python, a diferencia de otros lenguajes como C++, **no es necesario declarar el tipo de una variable**, simplemente se le asigna un valor y el entorno *"adivina"* automáticamente su tipo.

Además, el tipo de una variable puede cambiar durante la ejecución del programa, por ejemplo:

```
var = 3
# en este punto, el tipo de var es int
var = "hola"
# en este punto, el tipo de var es str
```

Por este hecho de que el tipo pueda mutar durante la ejecución, se dice que lenguajes como Python son **débilmente tipados** o **no tipados**, a diferencia de lenguajes **fuertemente tipados** como C++, donde se debe explicitar el tipo de una variable y respetarlo.

En principio puede parecer que utilizar un lenguaje débilmente tipado puede ser más rápido y cómodo (y generalmente lo es), pero también puede resultar confuso cuando existen muchas variables y, ya al no declarar el tipo, el entorno dispone de menos información para ayudarnos a encontrar errores. 

Se puede obtener el tipo de una variable en cualquier momento del programa utilizando la función *type()*, por ejemplo:

```
a = 3
type(a)
```

## El operador de asignación

El **operador de asignación** (=) es el operador más importante en cualquier lenguaje de programación. Permite **copiar el valor de la expresión a la derecha del operador dentro de la variable que está a la izquierda**, por ejemplo:

```
a = 3
c = 2 * a
```

En el primer caso se copia el valor de la **constante** ```3``` dentro de la **variable** ```a```.
En el segundo caso **primero se resuelve la expresión que está a la derecha del operador** (```2 * a``` que arroja el valor entero 6) y luego se coloca dicho valor dentro de la **variable** ```a```.

Es importante notar que a la izquierda del operador no puede haber otra cosa que no sea una variable, por ejemplo, la siguiente sentencia no es válida:

```
3 = 2 * a
```

## Conversiones





#??? Entrada y salida en Python

#??? Operadores relacionales


#??? Operadores lógicos


## Estructuras de control

### Estructuras condicionales


### Estructuras repetitivas


#??? Strings

In programming terms, we usually call text a string. When you
think of a string as a collection of letters, the term makes sense.

s = "Hola"

s = 'hola'


s = '''
alksjdla s
asda ksdjhas
a ksdjh
'''


Embedding Values in Strings
If you want to display a message using the contents of a vari-
able, you can embed values in a string using %s , which is like a
marker for a value that you want to add later. (Embedding values
is programmer-speak for “inserting values.”)
