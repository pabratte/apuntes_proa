# Ejercicios HTTP Forms

**IMPORTANTE:** cada ejercicio debe presentarse en una carpeta separada. Deben utilizarse
subcarpetas para hojas de estilo, imágenes, fuentes, etc.

### 1. Escriba su propio buscador

Si se envía un pedido de tipo GET a la dirección https://www.google.com/search, Google responde con la página de resultados de búsqueda. Cree una página con su propia interfaz para el buscador en la que incluya un formulario con:

* un campo de texto que permita al usuario ingresar el termino de búsqueda
* un botón para enviar el formulario a la dirección especificada anteriormente

**IMPORTANTE**: el campo en el que el servidor de Google espera recibir el término de la búsqueda debe tener por nombre: *q*.

Proporcione estilo al formulario agregando colores, imágenes, fuentes, etc.



### 2. Calculadora

Escriba una interfaz para una calculadora que permita realizar operaciones simples. El formulario debe tener los siguientes campos:

* *valor1*: un campo de tipo texto o numérico que permita al usuario ingresar el primer valor a operar
* *valor2*: un campo de tipo texto o numérico que permita al usuario ingresar el segundo valor a operar

* *op*: la operación a realizar entre *valor1* y *valor2*. Debe ser un campo de tipo **select**. Los valores que se deberán enviar al servidor deberán ser alguno de los siguientes: *"suma"*, *"resta"*, *"multip"* o *"div"*.
* un botón para enviar el formulario.

El pedido generado por el formulario debe ser de tipo POST y enviarse a la siguiente dirección: [https://formsexercise.herokuapp.com/calc](https://formsexercise.herokuapp.com/calc)

Proporcione estilo al formulario agregando colores, imágenes, fuentes, etc.



### 3. Formulario de Login

Escriba un formulario de login que tenga los siguientes campos:

* email: un campo de tipo texto o email que permita al usuario ingresar su correo electrónico
* *password*: un campo de tipo password que permita al usuario su contraseña

* *rememberme*: un checkbox con el label: *"Recordarme en este equipo"* que permita al usuario elegir si quiere o no que se rellenen automáticamente los datos la próxima vez que abra la página
* un botón con el texto: *"Ingresar"*, que permita enviar el formulario.

El pedido generado por el formulario debe ser de tipo POST y enviarse a la siguiente dirección: : [https://formsexercise.herokuapp.com/login](https://formsexercise.herokuapp.com/login)

El formulario debe estar dentro de una caja de color que debe aparecer centrada en la página. Además, debe utilizar una imagen o color de fondo para la página. Estilice el formulario agregando colores, imágenes, fuentes, etc.
