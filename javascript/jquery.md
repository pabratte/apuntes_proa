class: center, middle, inverse, layout
# JQuery

## Programación III

---

class: inverse
layout: true

---

## ¿Qué es?


jQuery is a fast, small, and feature-rich **JavaScript library**.
It makes things like HTML document traversal and manipulation, event handling, and animation much simpler.

---

## ¿Cómo incluir?

```html
<script src="https://code.jquery.com/jquery-3.1.1.js"></script>
```

---

## Sintáxis de jQuery
```javascript
$("<selector>").<operacion>() 
```

---

## Selectores

```javascript
$("p").hide()  // hides all <p> elements
$(".demo").hide()  // hides all elements with class="demo"
$("#demo").hide()  // hides the element with id="demo"
```

* JQuery utiliza los mismos selectores de CSS para recorrer el documento y buscar determinados elementos.
* Lo que devuelve es un **objeto wrapper** (envoltorio, testaferro), es decir, un objeto que representa ese elemento de la estructura HTML.
* Las operaciones que se hacen sobre ese elemento repercuten sobre el HTML.
* En el caso de que el **wrapper** represente a un grupo de elementos, la operación de hace sobre **todos ellos**.

---

## Otros selectores...

---

## Como empezar... (evento ready)

```javascript
$(document).ready(function() {
   // jQuery code goes here
});
```

ó también

```javascript
$(function() {
   // jQuery code goes here
});
```

* Esto se hace para que el código se ejecute **sólo** cuando ya se haya cargado todo el HTML.
* Lo vemos mejor en la parte de eventos.

---

## Atributos

¿Qué era un atributo?

```html
<a id="misuperenlace" href="http://www.jquery.com">Hace clic aquí</a>
```

* **elemento/etiqueta**: a
* **atributos** (lo que va dentro de la etiqueta): id, href
* **contenido**: Hace clic aquí

---

## Atributos

En jQuery los atributos se acceden/modifican mediante el método *attr()*


* attr() como getter: especifico el nombre del atributo cuyo valor quiero obtener (**no especifico el valor**)
```javascript
var a = $("#misuperenlace").attr("href");
alert(a)
```

* attr() como setter: especifico el nombre del atributo **y el valor que quiero que tenga**
```javascript
$("#misuperenlace").attr("href", "http://www.google.com");
```

---

## Setters y Getters

* **Setters**: modifican el valor de una propiedad
* **Getters**: obtienen el valor de una propiedad

En jQuery la mayoría de los métodos (funciones) sirven para hacer ambas cosas a la vez según la cantidad de parámetros que reciban. Por ejemplo: 1 único parámetro sirve para obtener el valor, 2 parámetros sirven para modificar el valor.

Ejemplo a continuación...
---

## Atributos

Eliminar el atributo (que no es lo mismo que ponerlo con un valor vacío)

```javascript
$("#mybutton").removeAttr("disabled");
```

Ejemplo: los botones aparecen como deshabilitados cuando está el atributo disabled (aunque tenga un valor vacío) 

```html
<button id="mybutton" disabled="">Enviar formulario</button>
```

---

## CSS

Se utiliza el método setter/getter: css()

```javascript
// getter
var c = $("p").css("color");
alert(c)

// setter
$("p").css("background-color", "red");
```
---

## CSS

Con un diccionario de propiedades

```javascript
// setter como diccionario de clave, valor
var props = {
  "background-color": "red",
  "color": "blue"
}
$("p").css(props);
```
---

## Clases CSS

```javascript
addClass("nombre-clase")
removeClass("nombre-clase")
```
Agregan o quitan la clase *nombre-clase* a el/los elementos seleccionados

```javascript
toggleClass("nombre-clase")
```

Si la tiene la elimina, si no la tiene la agrega

**OJO!** lo que recibe es el nombre de la clase NO el selector CSS(".nombre-clase")

---

## Eventos (parte 1)

*callback*: función que se ejecuta cuando ocurre algún evento.

Las funciones tienen el nombre del evento (por ejemplo *click*) y reciben un callback que se disparará automáticamente cuando ocurra el evento

**Son funciones que reciben como argumento a otra función (qué loco!)**

```javascript
// creo una función
function miFuncionCallback(){
  alert("Hice clic en el botón");
}

// cuando se haga click en el elemento con id=demo se ejecuta miFuncionCallback
$("#demo").click(miFuncionCallback);
```

ó también

```javascript
$("#demo").click(function() {
  alert("Hice clic en el botón")
});
```

---

## Ejercicio 1 

* Crear una página que contenga un elemento de imagen (img) y 2 botones
* La página debe utilizar Bootstrap (háganla linda)
* Los botones deben decir "Montaña" y "Playa", al hacer clic en cada uno debe cambiar la imagen del elemento img por la imagen de un paisaje de playa o de montaña respectivamente (cambiando el atributo src del elemento)

---

## Ejercicio 2

* Crear una página que contenga un elemento div con un texto cualquiera y 3 botones
* La página debe utilizar Bootstrap (háganla linda)
* Cada botón debe representar un color diferente
* Al hacer clic en cada botón, el div debe tomar el color de fondo que indica el botón


**OPCIONAL**
* Definir, mediante CSS, 3 clases de estilo diferente (color de tipografía, de fondo, tipo y color de borde, fuente, etc.)
* Cada botón, al hacerle clic, debe aplicar una de estas clases al div (utilizar addClass(), removeClass() o toggleClass())


---

# Manipular contenido

Manipular el contenido de un elemento:

* html: (setter o getter) acceder o manipular el contenido como **html**
* text: (setter o getter) acceder manipular el contenido como **texto**
* val: (setter o getter) acceder manipular los **valores** de los **campos de formularios** (input, select, textarea, etc) 

---

# Manipular contenido

Crear nuevo elemento

```
var nuevo = $("<p>Soy un párrafo</p>")
```
---

# Insertar un elemento

* append(): inserta el nuevo elemento, **dentro de un elemento**, **al final del mismo**
* prepend(): inserta el nuevo elemento, **dentro de un elemento**, **al principio del mismo**
* before(): inserta el nuevo elemento, **antes de un elemento**
* after(): inserta el nuevo elemento, **después de un elemento**


<div style="text-align:center;">
<img src="https://i.stack.imgur.com/GWmap.png">
</div>

---

# Ejemplo: lista de compras




# Eventos

click occurs when an element is clicked.
dblclick occurs when an element is double-clicked.
mouseenter occurs when the mouse pointer is over (enters) the selected element.
mouseleave occurs when the mouse pointer leaves the selected element.
mouseover occurs when the mouse pointer is over the selected element.

Keyboard Events:
keydown occurs when a keyboard key is pressed down.
keyup occurs when a keyboard key is released.

Form Events:
submit occurs when a form is submitted.
change occurs when the value of an element has been changed.
focus occurs when an element gets focus.
blur occurs when an element loses focus.

Document Events:
ready occurs when the DOM has been loaded.
resize occurs when the browser window changes size.
scroll occurs when the user scrolls in the specified element.
