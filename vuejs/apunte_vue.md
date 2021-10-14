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
