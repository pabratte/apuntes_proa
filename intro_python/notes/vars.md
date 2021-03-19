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