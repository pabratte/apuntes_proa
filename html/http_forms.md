# Formularios HTML

## ¿Cómo funciona la web?

###  Protocolo HTTP

<center>
<img style="width: 80%;" src="img/HTTP.png">
</center>

HTTP, de sus siglas en inglés: "Hypertext Transfer Protocol", es el nombre de un protocolo el cual nos permite realizar una petición de datos y recursos, como pueden ser documentos HTML. Es la base de cualquier intercambio de datos en la Web, y un protocolo de estructura cliente-servidor, esto quiere decir que una petición de datos es iniciada por el elemento que recibirá los datos (el cliente), normalmente un navegador Web.

* **Cliente**: quien solicita un recurso (navegador, teléfono, compu)
* **Servidor**: computadora que está continuamente escuchando y respondiendo pedidos de los clientes
---

# Protocolo HTTP
<center>
<img style="width: 80%;" src="img/HTTP_Steps.png">
</center>
* Los pedidos (request) y las respuestas (response) consisten en **texto** con un formato específico.

* Generalmente tienen una cabecera, luego una línea en blanco (blank line) y luego datos (payload).
* En el caso de la respuestas, los datos consisten en el **código HTML** que el navegador mostrará. Por ejemplo:

<center>
<img src="img/HTTP_RequestResponseMessages.png" width="80%">
</center>

---

* Una vez que el browser recibe el HTML la conexión con el servidor se corta.
* Por cada recurso dentro del HTML (imagen, hoja de estilo, script) se establece una nueva conexión. Se puede ver un ejemplo de esto en el inspector del navegador.


## Tipos de pedidos

Existen varios tipos de pedidos, los más importantes son el tipo GET y el tipo POST.

* HTTP: GET
  - Sirven para **SOLICITAR** información al servidor.
  - Los datos que se envían al servidor se escriben en la misma dirección URL, ejemplo: 
  	```www.ejemplo.com/registrarse.php?nombre=pedro&apellido=perez&edad=55&sexo=masculino```
  	La longitud de las URL es limitada: 2000 caracteres (no se pueden enviar muchos datos, ni binarios (audio, imagenes, etc).
  - Los pedidos de tipo GET se cachean (¿qué es cache?)
  - Los pedidos GET se generan al hacer clic sobre un enlace o escribir una dirección en la barra de direcciones.
  
* HTTP: POST
  - Sirven para **ENVIAR** información al servidor. 
  - Los datos no se envían en la URL sino en un payload (un anexo) al pedido. Lo cual otorga mayor seguridad porque se pueden encriptar.
  - Los pedidos de tipo POST NO se guardan en cache ni en el historial (ventana de reenviar datos).
  - Longitud ilimitada para los datos que se envían (payload) 
  - Los pedidos POST se pueden generar mediante formularios.

## Formularios

Permiten generar pedidos (GET, POST, etc)

```html
<form method="POST" action="www.google.com">
    <label>Nombre: </label>
	<input type="text" name="nombre">
    <label>Edad: </label>
	<input type="number" name="edad">
    <input type="submit" value="Enviar datos">
</form>
```

Atributos de la etiqueta <form>:

* method: el método del pedido (GET, POST)
* action: la URL hacia donde se envía el pedido

Al enviar un formulario (submit) se genera un pedido (GET o POST) en el que se incluye la información de todas las etiquetas <input> que se encuentren dentro del formulario. Los valores enviados se identifican por el campo **name**. Por ejemplo, el formulario anterior produciría un pedido POST similar al siguiente:

#### Ejemplo de pedido POST

```
POST / HTTP/1.1
Host: www.google.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 19

nombre=Juan&edad=23
```

#### Ejemplo de pedido GET

```
GET /nombre=Juan&edad=23 HTTP/1.1
Host: www.google.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 19
```



### Tipos de input

* **text**: un campo que permite al usuario escribir texto

  ```html
  <label>Nombre de usuario</label><br>
  <input type="text" name="username">
  ```

* **number**: un campo que permite ingresar sólo valores numéricos

  ```html
  <label>Edad</label><br>
  <input type="number" name="edad">
  ```

* **password**: un campo de texto que oculta los caracteres escritos

  ```html
  <label>Contraseña</label><br>
  <input type="password" name="password">
  ```

* **radio**: es un control que permite seleccionar entre múltiples opciones. Todas las opciones se muestran pero sólo una se puede seleccionar al mismo tiempo. Es útil cuando las opciones son pocas. **Para que sólo pueda seleccionarse una opción el valor name debe ser el mismo en todos los input**

  ```html
  <label>Masculino</label><br>
  <input type="radio" name="sexo" value="masculino">
  <label>Femenino</label><br>
  <input type="radio" name="sexo" value="femenino">
  ```

* **checkbox**: es una caja que puede estar tildada o destildada. **IMPORTANTE** el valor especificado sólo se envía si la caja está tildada (de lo contrario no se envía ese dato). El valor enviado es *on*.

  ```html
  <label>Recordarme en este equipo:</label>
  <input type="checkbox" name="rememberme">
  ```

  

* **submit**: es un botón que envia los datos del formulario. El valor de *value* es lo que figura como etiqueta del botón.

  ```html
  <input type="submit" value="Enviar datos">
  ```

* **select**: lista desplegable que permite seleccionar una de las opciones disponibles. Es útil cuando las opciones son muchas y ocuparía demasiado lugar mostrarlas a todas juntas. Notar que cada opción tiene un valor (*value*) y un contenido que es el texto que se muesta. El valor que se envía con el formulario es el campo *value* (no el contenido) de la opción seleccionada. 

  ```html
  <label>País</label><br>
  <select name="pais">
  	<option value="arg">Argentina</option>
  	<option value="bra">Brasil</option>
  	<option value="uru">Uruguay</option>
  	<option value="chi">Chile</option>
  </select>
  ```

  

Referencia: https://www.w3schools.com/html/html_form_input_types.asp

# Ejercicios

### Escriba su propio Google

Si se envía un pedido de tipo GET a la dirección https://www.google.com/search, Google responde con la página de resultados de búsqueda. Cree una página con su propia interfaz para el buscador en la que incluya un formulario con:

* un campo de texto que permita al usuario ingresar el termino de búsqueda
* un botón para enviar el formulario a la dirección especificada anteriormente

**IMPORTANTE**: el campo en el que el servidor de Google espera recibir el término de la búsqueda debe tener por nombre: *q*.

Estilice el formulario agregando colores, imágenes, fuentes, etc.



### Calculadora

Escriba una interfaz para una calculadora que permita realizar operaciones simples. El formulario debe tener los siguientes campos:

* *valor1*: un campo de tipo texto o numérico que permita al usuario ingresar el primer valor a operar
* *valor2*: un campo de tipo texto o numérico que permita al usuario ingresar el segundo valor a operar

* *op*: la operación a realizar entre *valor1* y *valor2*. Debe ser un campo de tipo <select>. Los valores que se deberán enviar al servidor deberán ser alguno de los siguientes: *"suma"*, *"resta"*, *"multip"* o *"div"*.
* un botón para enviar el formulario.

El pedido generado por el formulario debe ser de tipo POST y enviarse a la siguiente dirección: ??????????

Estilice el formulario agregando colores, imágenes, fuentes, etc.



### Formulario de Login

Escriba un formulario de login que tenga los siguientes campos:

* email: un campo de tipo texto o email que permita al usuario ingresar su correo electrónico
* *password*: un campo de tipo password que permita al usuario su contraseña

* *rememberme*: un checkbox con el label: *"Recordarme en este equipo"* que permita al usuario elegir si quiere o no que se rellenen automáticamente los datos la próxima vez que abra la página
* un botón con el texto: *"Ingresar"*, que permita enviar el formulario.

El pedido generado por el formulario debe ser de tipo POST y enviarse a la siguiente dirección: ??????????

El formulario debe estar dentro de una caja de color que debe aparecer centrada en la página. Además, debe utilizar una imagen o color de fondo para la página. Estilice el formulario agregando colores, imágenes, fuentes, etc.