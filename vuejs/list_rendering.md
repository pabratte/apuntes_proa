## List rendering

La directiva **v-for** permite recorrer una lista y renderizar elementos o componentes por cada elemento dentro de la misma. Por ejemplo:

```html
<template>
  <ul>
  	<li v-for="i in items" :key="i">{{i}}<li>
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

**IMPORTANTE**: notar que cuando se utiliza **v-for** es necesario incluir el atributo **key** (con :key o v-key). El mismo sirve para especificar un identificador único para cada elemento. Vue necesita ese identificador para saber qué elementos del HTML debe actualizar.


### Ejercicio #4
Programe una aplicación de tipo lista de compras, la misma deberá tener:

* Un input en el que el usuario deberá escribir el nombre de un nuevo item</li>
* Un botón que al ser presionado agregue el nuevo item a la lista</li>
* La lista desordenada (ul) con todos los elementos agregados por el usuario</li>


Además, en caso de no haber ningún elemento dentro de la lista debe aparecer en su lugar el mensaje *"No hay nada en la lista"*. Para ello se sugiere usar renderizado condicional.
