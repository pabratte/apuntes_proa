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

Una aplicación/componente de Vue tiene al menos las siguientes partes (existen también otras):

+ **name**: es el nombre del componente/aplicación. 

* **data**: es **una función** que devuelve **un diccionario** con los datos del componente.
* **methods**: son las funciones que el usuario va a ejecutar. Las funciones modifican los datos del componente.
