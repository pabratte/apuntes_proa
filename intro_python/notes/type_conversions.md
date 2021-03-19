
## Conversiones

¿Qué ocurre cuando se trata de realizar una operación sobre variables/constantes que poseen tipos diferentes? Por ejemplo:

```
a = 3/5.0
b = "Hola" + 7.5
```

### Conversiones implícitas

Son las conversiones que realiza automáticamente el intérprete.

**Para realizar una operación es necesario que todos los datos que intervienen sean del mismo tipo. Si no es así, el intérprete buscará convertir todos los datos a un mismo tipo antes de operar.**

Ejemplos:

```
a = 3/5
print(a)
```
Devuelve 0, ya que 5 y 3 son enteros y el resultado de dividirlos es 0 (y sobran 3).


```
b = 3
a = b/5.0
print(a)
```
Muestra 0.6, el valor de b (3, entero) es convertido a *float* para poder operarlo con 5.0 (que es *float*).

```
b = "Hola" + 7.5
```
La expresión arroja el siguiente error.

```
TypeError: cannot concatenate 'str' and 'float' objects
```
El intérprete no puede convertir automáticamente la cadena *"Hola"* en un número, ni tampoco puede traducir el valor *float* 7.5 a una cadena de texto (al menos no automáticamente). Por lo tanto, no se puede aplicar el operador (+) a datos de tipo *str* y *float*.


### Conversiones explícitas

A diferencia de los casos anteriores, en los que el intérprete realiza las conversiones de tipo de manera automática sin notificar al programador, el programador puede especificar determinadas conversiones de datos que desee hacer, este tipo de conversiones se llaman **conversiones explícitas** y se hacen mediante funciones nombradas como los tipos y que reciben como argumento la expresión a convertir. Por ejemplo:

```
a = 3/float(5)
print(a)
```

En este caso el 5 (**int**) es convertido explicitamente a **float**, por lo cual el intérprete se ve forzado a realizar también una conversión implícita a **float** del valor 3. 

```
b = "Hola" + str(7.5)
```

En este caso la conversión explícita del valor 7.5 a string sí funciona, por lo que el resultado del operador (+) es la concatenación de ambas cadenas (es decir: "Hola7.5").
