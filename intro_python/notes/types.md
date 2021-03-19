## Tipos de datos

Cada dato que forma parte de un programa, tanto las variables como las constantes, **tienen un tipo asociado** (entero, real, cadena de texto, etc).

Algunos de los tipos de datos principales en Python son

* *int*
* *float*
* *str* (string)
* *bool*

Debajo se muestran ejemplos de variables para cada uno de estos tipos.

```
i = 3
f = 7.1
s1 = "hola"
s2 = 'chau' # también se puede usar comillas simples 
b = True
```

**El tipo de un dato es importante porque indica qué operaciones se pueden hacer con el mismo**. Por ejemplo, se puede sumar números enteros o reales, pero no se puede sumar cadenas de texto o valores de verdad (booleanos).

En Python, a diferencia de otros lenguajes como C++, **no es necesario declarar el tipo de una variable**, simplemente se le asigna un valor y el entorno *"adivina"* automáticamente su tipo.

Además, el tipo de una variable puede cambiar durante la ejecución del programa, por ejemplo:

```python
var = 3
# en este punto, el tipo de var es int
var = "hola"
# en este punto, el tipo de var es str
```

Por este hecho de que el tipo pueda mutar durante la ejecución, se dice que lenguajes como Python son **débilmente tipados** o **no tipados**, a diferencia de lenguajes **fuertemente tipados** como C++, donde se debe explicitar el tipo de una variable y respetarlo.

En principio puede parecer que utilizar un lenguaje débilmente tipado puede ser más rápido y cómodo (y generalmente lo es), pero también puede resultar confuso cuando existen muchas variables y, ya al no declarar el tipo, el entorno dispone de menos información para ayudarnos a encontrar errores. 

Se puede obtener el tipo de una variable en cualquier momento del programa utilizando la función *type()*, por ejemplo:

```python
a = 3
type(a)
```