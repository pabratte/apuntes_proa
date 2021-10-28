### Ejercicio #5

Agregue a la aplicación de la lista de compras la posibilidad de agregar la cantidad de unidades que se debe comprar de un determinado item. Para ello agregue un input adicional que permita especificar dicha cantidad.

Además, antes de agregar el item a la lista **valide** que el usuario haya ingresado valores válidos en las entradas. Para la validación tenga en cuenta que el nombre del item no debería estar vacío y que la cantidad ingresada para el producto debería ser un número válido.

Ejemplo:



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


