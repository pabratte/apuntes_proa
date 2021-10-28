## Components

Los componentes son pedazos **reutilizables** de una aplicación. La importancia de los componentes no es sólo la reutilización sino también la distribución de responsabilidad y la separación de un problema grande en problemas más pequeños (un componente se concentra en resolver una pequeña parte del problema).

Además, los componentes permiten **encapsular** pedazos de la interfaz gráfica. 

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

## Props

Las **props** (propiedades) son formas de que el componente padre pase información al componente hijo. Las props permiten **parametrizar** un componente, permitiendo que tenga distinto aspecto o comportamientos según los valores especificados.

Las **props** se declaran como una sección más del componente, y su valor es un arreglo de strings. Se pueden utilizar como si fueran variables que se declararon dentro de la sección *data* (aunque en realidad son especificados al instanciar el componente).

```html
<template>
  <button v-bind:style="{ background-color: color}" @click="cont=cont+1">{{label}} ({{cont}})</button>
</template>

<script>
export default {
  name: 'BotonContador',
  props:[
      'label',
      'color'
  ]
  data: function(){
    return {
      cont: 0
    }
  },
}
</script>
```

Las props se especifican como atributos a la hora de instanciar el componente dentro del componente padre:


```html
<template>
  <div id="app">
    <BotonContador label="Jamón y queso" color="red"/>
    <BotonContador label="Carne dulce" color="blue"/>
  </div>
</template>
```

### Ejercicio #7

Crear la EmpanadApp, una app para llevar el registro de un pedido de distintos sabores de empanadas en una juntada. La app consiste en diversos botones, uno para cada sabor de empanada disponible. Cada botón posee además un contador que almacena la cantidad de empanadas que se deben pedir de dicho sabor. De esta manera, cada comensal debe presionar sobre el botón correspondiente a los sabores de empanadas que desea consumir.