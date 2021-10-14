## Introducción a Javascript

## El DOM

El Document Object Model es un modelo estándar sobre acceder, crear, modificar o eliminar los elementos de un documento HTML desde Javascript.

Es un conjunto de objetos (variables) que permiten acceder desde Javascript a los elementos de un documento HTML.

<img src="https://www.w3schools.com/js/pic_htmltree.gif"> 

## Ejemplo de programa con vanilla javascript

Vanilla Javascript => Javascript puro y duro, sin bibliotecas ni nada que facilite las cosas.

```html
<!DOCTYPE html>
<html lang="en">
<body>
    <label>Ingrese su nombre</label>
    <input class="entrada" type="text" id="input_name">
    <button onclick="sayHello()">Saludar</button>
    <div id="greeting"></div>
    <script>
        function sayHello(){
            // get input element
            var input_elem = document.getElementById("input_name")
            // get text from input element
            var user_name = input_elem.value
            // calculate string
            var output_string = "Hello " + user_name + "!!!"
            // get output element
            var output_elem = document.getElementById("greeting")
            // write string to output element
            output_elem.textContent = output_string
        }
    </script>
</body>
</html>
```



# Vue.js

## Tecnologías que vamos a usar

* **Node.js**: Javascript runtime environment, es para poder ejecutar Javascript fuera del navegador, ya que todas las herramientas que vamos a utilizar están hechas con Javascript.
* **NPM**: Node package manager, para instalar y gestionar bibliotecas.
* **[Webpack](https://webpack.js.org/)**: Module bundler. Articula el funcionamiento de las otras herramientas (por ejemplo Babel). Crea un paquete (bundle) concatenando todos los archivos de código en uno sólo.
* **Typescript**: Lenguaje de programación creado por Microsoft. Es como Javascript pero agrega mejoras (tipos). Como el navegador sólo entiende Javascript y no Typescript, necesitamos una herramienta que haga la traducción desde el segundo al primero (Babel).
* **Babel**: Transpilar (traducir de un lenguaje a otro).
* **vue-cli**: (npm install -g @vue/cli) Aplicación de consola para crear proyectos de Vue.js

## Introducción a Vue.js

Es un framework de JavaScript de código abierto para la construcción de **interfaces de usuario** y aplicaciones de una sola página (SPA). Se ejecuta en el cliente (el navegador).

## Ejecutar un proyecto de Vue.js

```
# instalar dependencias
npm install

# ejecutar el proyecto (live server)
npm run serve
```

## Estructura de archivos de un proyecto en Vue.js

![](vue_files.jpg)

* Los archivos de código se encuentran dentro del directorio **src**
* Los archivos de Vue.js tienen la extensión .vue
* 

## Estructura de un componente de Vue.js

Una aplicación (o componente) de vue está compuesto por 3 secciones:

* **template** o plantilla: es el código HTML del componente.
* **script**: el código de la aplicación.
* **style**: los estilos utilizados para ese componente.

```html
<template>
  <div>
    Vue base app
  </div>
</template>

<script>
export default {
  name: 'Main',
  data: function(){
    return {
      // put your variables here...
    }
  },
  methods: {
    // put your methods here...
  }
}
</script>

<style>

</style>
```

**IMPORTANTE**: el navegador NO ENTIENDE de archivos con esta estructura. La herramienta Webpack, a partir de estos archivos, generará los correspondientes HTML, CSS y JS.

## Estructura del código de una aplicación en Vue

Tiene al menos las siguientes partes (existen también otras):

+ **name**: es el nombre del componente/aplicación. 

* **data**: es **una función** que devuelve **un diccionario** con los datos del componente.
* **methods**: son las funciones que el usuario va a ejecutar. Las funciones modifican los datos del componente.

## Text interpolation

Dentro del template HTML se puede usar la siguiente sintaxis para reemplazar el contenido de las etiquetas por valores de las variables.

```html
<template>
  <div>
    Hola, mi nombre es {{nombre}}
  </div>
</template>

<script>
export default {
  name: 'Main',
  data: function(){
    return {
      nombre: "Juan"
    }
  }
}
</script>
```

**IMPORTANTE**: si el valor de la variable se modifica, Vue se encarga automáticamente de actualizar el HTML, por eso se dice que es reactivo (reacciona automáticamente ante los cambios).

## Two Way Data Binding

El atributo ```v-model``` permite establecer una **asociación bidireccional entre un input y una variable** de manera que:

* Si el usuario modifica el input, se modifica el valor de la variable.
* Si se modifica la variable, cambia automáticamente el valor del input.

```html
<template>
  <div>
  	<label>Ingrese un número: </label>
  	<input v-model="num">
  	<p>Usted ingresó {{num}}!</p>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data: function(){
    return {
      num: 0
    }
  }
}
</script>
```

<div style="background-color: lightsteelblue; color: darkstalegray; padding: 10px; border-radius: 3px;">
<p>Tomar como base la aplicación del repositorio: <a href="https://github.com/pabratte/vue-base-app">https://github.com/pabratte/vue-base-app</a>. Hacer un <b>fork</b> del repositorio y luego <b>clonarlo</b>.    
</p>
<b>Ejercicio #1</b>: Crear un programa que permita al usuario ingresar su nombre y lo salude.
Para ello realice los siguientes pasos:
<ul>
	<li>Cree un nuevo archivo en la carpeta <i>components</i> llamado <i>Ejercicio1.vue</i>
	<li>En el archivo <i>App.vue</i> reemplaze la etiqueta &lt;Main /&gt; por &lt;Ejercicio1 /&gt;
	<li>En el archivo <i>Ejercicio1.vue</i>:
		<ul>
			<li>Coloque las etiquetas para las 3 secciones (template, script y style)</li>
			<li>Dentro de la etiqueta template declare los elementos HTML (input, label, etc.)</li>
			<li>Dentro de la etiqueta script exporte los datos del componente (name: "Ejercicio1" y en data coloque una variable que se utilizará para almacenar el nombre ingresado por el usuario)</li>
			<li>Utilice la directiva v-model para asociar la variable al input</li>
			<li>Dentro del template utilizar interpolación de texto para mostrar el valor de la variable</li>
		</ul>
</ul>
</div>

## Events

Se puede hacer que, ante un evento, se ejecute uno de los métodos del componente. Para eso hace falta:

* Crear la función *callback* dentro de la sección **methods** del componente

* Utilizar la directiva v-on en el elemento en el que se desea captar el evento.


```html
<template>
  <div>
  	<label>Hola: {{name}}</label>
  	<button v-on:click="onClick()">Haceme clic</button>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data: function(){
    return {
      name: "Juan"
    }
  },
  methods: onClick(){
    alert("Clic en el botón")
    this.name = "Pablo"
  }
}
</script>
```

**IMPORTANTE**: para acceder a una variable del componente desde un método del mismo se debe anteponer **.this**. Esto indica que nos referimos a la variable que fue declarada como dato del componente y no a una variable local de la función.

<div style="background-color: lightsteelblue; color: darkstalegray; padding: 10px; border-radius: 3px;">
<b>Ejercicio #2</b>: Crear una pequeña calculadora que posea:
<ul>
    <li>Dos campos de tipo input para ingresar los números</li>
    <li>Un campo de tipo select para seleccionar la operación</i>
    <li>Un botón que al ser presionado muestre el resultado de la operación</i>
</ul>
<b>IMPORTANTE:</b> El ejercicio debe ser creado y agregado a la aplicación como un nuevo componente.
<b>Ayuda:</b> Puede desarrollar el ejercicio de manera progresiva haciendo que la calculadora sólo sirva para sumar y agregar el select para las distintas operaciones luego.
</div>

## Components

Los componentes son pedazos **reutilizables** de una aplicación. La importancia de los componentes no es sólo la reutilización sino también la distribución de responsabilidad y la separación de un problema grande en problemas más pequeños (un componente se concentra en resolver una pequeña parte del problema).

Cuando declaramos un componente debemos especificar su nombre (atributo: **name**):

```html
<template>
  <div>

  </div>
</template>

<script>
export default {
  name: 'Ejercicio1',
  data: function(){
    return {
      name: "Juan"
    }
  },
}
</script>
```

A la hora de utilizar un componente desde otro (este último se llama **componente padre**), es necesario:
* Importarlo (con *import*)
* Declararlo en el campo *components* del padre
* Instanciarlo (usarlo dentro del template HTML)

```html
<template>
  <div id="app">
    <h1>Ejercicio 1</h1>
    <Ejercicio1 />
    <Ejercicio2 />
  </div>
</template>

<script>
import Ejercicio1 from "./components/Ejercicio1"
import Ejercicio2 from "./components/Ejercicio2"

export default {
  components: {
    Ejercicio1,
    Ejercicio2,
  },
  name: 'App',
}
</script>

<style>

</style>
```

**IMPORTANTE**: Respetar las siguientes reglas de estilo:

* Los nombres de los componentes van en **PascalCase** (primera letra en mayúscula y primera letra de cada palabra también en mayúscula)
* El archivo del componente con se debe llamar igual que el componente

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

<div style="background-color: lightsteelblue; color: darkstalegray; padding: 10px; border-radius: 3px;">
<b>Ejercicio #3</b>: Tomando como base la calculadora diseñada en el ejercicio anterior, compruebe que el contenido de las entradas de datos sea un número y utilice renderizado condicional para mostrar mensajes de error.
<br>
<b>Ayuda:</b> Para realizar las comprobaciones puede usar <a href="https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/parseInt">parseInt()</a>.
<br>
<b>Desafío extra:</b> Además de mostrar los mensajes de error, deshabilite el botón para realizar el cálculo en el caso de que lo que haya ingresado el usuario no sea un número.
</div>


## v-for

La directiva **v-for** permite recorrer una lista y renderizar elementos o componentes por cada elemento dentro de la misma. Por ejemplo:

```html
<template>
  <ul>
  	<li v-for="i in items">{{i}}<li>
  </ul>
</template>

<script>
export default {
  name: 'App',
  data: function(){
    return {
      items: ["mazanas", "peras", "bananas"]
    }
  },
}
</script>
```


<div style="background-color: lightsteelblue; color: darkstalegray; padding: 10px; border-radius: 3px;">
<b>Ejercicio #4</b>: Programe una aplicación de tipo lista de compras, la misma deberá tener:
<ul>
<li>Un input en el que el usuario deberá escribir el nombre de un nuevo item</li>
<li>Un botón que al ser presionado agregue el nuevo item a la lista</li>
<li>La lista desordenada (ul) con todos los elementos agregados por el usuario</li>
</ul>
Además, en caso de no haber ningún elemento dentro de la lista debe aparecer en su lugar el mensaje <i>"No hay nada en la lista"</i>. Para ello se sugiere usar renderizado condicional.
</div>

<div style="background-color: lightsteelblue; color: darkstalegray; padding: 10px; border-radius: 3px;">
<b>Ejercicio #5</b>: Agregue a la aplicación de la lista de compras la posibilidad de agregar la cantidad de unidades que se debe comprar de un determinado item. Para ello agregue un input adicional que permita especificar dicha cantidad.
Además, antes de agregar el item a la lista valide que el usuario haya ingresado valores válidos en las entradas.
Por ejemplo:
</div>

```html
<template>
  <ul>
  	<li v-for="i in items">{{i.name}} x {{i.quantity}}<li>
  </ul>
</template>

<script>
export default {
  name: 'App',
  itemName: '',
  itemQuant: '',
  data: function(){
    return {
      items: []
    }
  },
  methods: addNewItem(){
  	var newItem = {
  		name: this.itemName,
  		quantity: this.itemQuant
  	}
  	this.items.push(newItem)
  }
}
</script>
```

<div style="background-color: lightsteelblue; color: darkstalegray; padding: 10px; border-radius: 3px;">
<b>Ejercicio #6</b>: Agregue a la aplicación de lista de compra la posibilidad de eliminar items. Para ello agregue al lado de cada item un botón que permita eliminarlo de la lista. Al hacer clic en el botón se debe llamar a la función deleteItem(itemId). La función recibe el id del item a eliminar y lo quita de la lista. Una vez eliminado el item Vue se encargará de actualizar automáticamente el HTML de la página. Para la función deleteItem() puede tomar como ejemplo el código siguiente.
</div>

```javascript
function deleteItem(itemId){
	this.items = this.items.filter((item) => item.id !== itemId)
}
```

**IMPORTANTE**: notar que para que el código anterior funcione correctamente la lista de items se debe llamar *items* y dentro de la misma el id de cada componente debe estar almacenado en el campo *id* .