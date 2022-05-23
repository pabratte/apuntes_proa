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
  methods: {
    onClick(){
      alert("Clic en el botón")
      this.name = "Pablo"
    }
  }
}
</script>
```

**IMPORTANTE**: para acceder a una variable del componente desde un método del mismo se debe anteponer **.this**. Esto indica que nos referimos a la variable que fue declarada como dato del componente y no a una variable local de la función.

### Ejercicio #2
Crear una pequeña calculadora que posea:

* Dos campos de tipo input para ingresar los números
* Un campo de tipo select para seleccionar la operación
* Un botón que al ser presionado muestre el resultado de la operación

**IMPORTANTE:** El ejercicio debe ser creado y agregado a la aplicación como un nuevo componente.

**Ayuda:** Puede desarrollar el ejercicio de manera progresiva haciendo que la calculadora sólo sirva para sumar y agregar el select para las distintas operaciones luego.
