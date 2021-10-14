## Ejercicio #6

Agregue a la aplicación de lista de compra la posibilidad de eliminar items.
Para ello tenga en cuenta lo siguiente:

* Cada item debe tener un campo *id* para distinguirlo de manera unívoca del resto. El valor de *id* es único para cada item. Para poder eliminar correctamente un item, es necesario poder identificarlo de manera unívoca. Por ejemplo, la siguiente función permite generar un UUID (Universally Unique IDentifier) que puede usarse como id de un nuevo item agregado a la lista.

```javascript
function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}
```
Tomado de [StackOverflow](https://stackoverflow.com/questions/105034/how-to-create-a-guid-uuid).

* En la interfaz, agregue al lado del nombre de cada item un botón que permita eliminarlo de la lista. Al hacer clic en el botón se debe llamar a la función deleteItem(itemId). La función recibe el *id* del item a eliminar y lo quita de la lista. Para eliminar un item de la lista se puede usar la siguiente función. 

```javascript
function deleteItem(itemId){
	this.items = this.items.filter((item) => item.id !== itemId)
}
```
Lo que hace la función anterior es utilizar filter() para crear una nueva lista incluyendo sólo algunos de los elementos (todos los que tengan un *id* distinto al especificado). notar que **para que el código anterior funcione correctamente** la lista de items se debe llamar *items* y dentro de la misma el id de cada componente debe estar almacenado en el campo *id* .

**IMPORTANTE**: una vez eliminado el item de la lista Vue se encargará de actualizar automáticamente el HTML de la página.
 
