class: center, middle, inverse, layout
# Introducción a Javascript

## Programación III

---

class: inverse
layout: true

---

# ¿Cómo funciona la web?

---



# Protocolo HTTP
<center>
<img src="img/HTTP.png">
</center>

* **Cliente**: quien solicita un recurso (navegador, teléfono, compu)
* **Servidor**: computadora que está continuamente escuchando y respondiendo pedidos de los clientes
---

# Protocolo HTTP
<center>
<img src="img/HTTP_Steps.png" width="100%">
</center>

---

# Protocolo HTTP
<center>
<img src="img/HTTP_RequestResponseMessages.png" width="100%">
</center>

---

# Protocolo HTTP

* Una vez que el browser recibe el HTML la conexión con el servidor se corta
* Por cada recurso dentro del HTML (imagen, hoja de estilo, script) se establece una nueva conexión

* Ejemplo -> Ver en el inspector

---

# Programación de aplicaciones web

* Del lado del servidor (backend)
	- Servidores estáticos
	- Páginas web dinámicas

* Del lado del cliente (frontend)
	- HTML (meh... no es lenguaje de programación)
	- CSS (meh... no es lenguaje de programación)
	- Javascript (único lenguaje de programación que entiende el navegador)
	
---

# Javascript

* Lenguaje de programación del lado del **cliente** (¿Qué significa?).
* **Único lenguaje que entienden los navegadores**
* Interpretado
* Débilmente tipado
* Sintáxis muy parecida a C++

---

# Javascript

## Incluir un script en una página

* Dentro de **head**

```
<html>
	<head>
		<script>
		// tu código aquí...
		</script>
	</head>
	<body>
	</body>
</html>
```

---

# Javascript

## Incluir un script en una página

* Al final del **body**
* Así nos aseguramos de que todo el contenido de la página se cargue antes que el script

```
<html>
	<head>
		
	</head>
	<body>
		<div class="container"></div>
		<script>
		// tu código aquí...
		</script>
	</body>
</html>
```

---

# Javascript

## Incluir un script externo

* Los archivos de Javascript llevan la extensión .js
```
script src="mi_app.js"></script>
	
```


---

# Javascript

## Variables

* Las variables se declaran con **var**
* Las reglas para nombrar variables son las mismas que en todos los lenguajes
	- Deben empezar con letra
	- No pueden tener espacios
	- No pueden ser palabras reservadas (if, else, while)
	- No se puede usar símbolos "raros" (@#?/$%&=)

```
var x = 10;		// número (no distingue entre float e int)
var y = "hola";	// string
```
---

# Javascript

## Salida

* alert()
* console.log()
* document.write()

```
var x = 10;
alert(x);
console.log("x vale: "+x);
document.write("<div>"+x+"</div>");
```

---

# Javascript

## Conversiones de tipo

¿Cuál es la salida del siguiente código?
```
var x = "50";
var y = "100.5";
alert(x+y);
```
---

# Javascript

## Conversiones de tipo

¿Cuál es la salida del siguiente código?

```
var a = "50";
var b = "100.5";
x = parseInt(a);
y = parseFloat(a);
alert(x+y);
```

---

# Javascript

## Otros tipos

* NaN (Not A Number)
```
var a = "ajksdjahsg";
var b = parseInt(a);
alert(b);
```
* undefined (la variable se declaró pero nunca se le dió valor)
```
var c;
alert(c);
```
* null (valor específico que signigica nada, nulo, ni siquiera es cero porque 0 != null)
```
var d;
d = null;
alert(d);
```


