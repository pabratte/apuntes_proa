
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

### Ejercicio #1
Crear un programa que permita al usuario ingresar su nombre y lo salude.
Para ello realice los siguientes pasos:

* Cree un nuevo archivo en la carpeta *components* llamado *Ejercicio1.vue*
* En el archivo *App.vue* reemplaze la etiqueta <Ejercicio1 />
* En el archivo *Ejercicio1.vue*:
	- Coloque las etiquetas para las 3 secciones (template, script y style)
	- Dentro de la etiqueta template declare los elementos HTML (input, label, etc.)
	- Dentro de la etiqueta script exporte los datos del componente (name: "Ejercicio1" y en data coloque una variable que se utilizará para almacenar el nombre ingresado por el usuario)
	- Utilice la directiva v-model para asociar la variable al input
	- Dentro del template utilizar interpolación de texto para mostrar el valor de la variable
