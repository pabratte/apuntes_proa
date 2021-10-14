## Conditional Rendering

Se puede decidir si un componente o una parte de la plantilla debe renderizarse mediante la directiva **v-if**. La misma recibe un valor o una expresión **lógica** (verdadero o falso) que determinará si el elemento se dibuja o no.

```html
<h1 v-if="ok">Sí</h1>
```
El elemento **h1** sólo se dibujará si el valor de la variable *ok* es *true*. De la misma manera puede utilizarse la directiva **v-else** para dibujar otra cosa en caso de que la condición resulte falsa.

```html
<h1 v-if="ok">Sí</h1>
<h1 v-else>No</h1
```

La directiva **v-show** funciona de manera similar a **v-if** (aunque v-show no soporta else).

**La diferencia entre *v-if* y *v-show* es que el primero quita el componente del DOM mientras que el segundo sólo lo oculta**.

### Ejercicio #3

Tomando como base la calculadora diseñada en el ejercicio anterior, compruebe que el contenido de las entradas de datos sea un número y utilice renderizado condicional para mostrar mensajes de error.

**Ayuda:** Para realizar las comprobaciones puede usar [parseInt()](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/parseInt).

**Desafío extra:** Además de mostrar los mensajes de error, deshabilite el botón para realizar el cálculo en el caso de que lo que haya ingresado el usuario no sea un número.

