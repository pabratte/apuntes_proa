<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/1280px-Git-logo.svg.png" style="width: 50%">

# Apunte Git

### 1. Instalar git

Descargar el instalador desde [aquí](https://git-scm.com/). Las opciones por defecto del instalador están bien.

### 2. Configurar usuario y email

Git necesita esta información para saber quién hace los commits. Sólo necesitaremos correr estos comandos por única vez.

```bash
git config --global user.name "<your-full-name>"
git config --global user.email "<your-email-address>
```

Se debe reemplazar `your-full-name`por el nombre completo del usuario y `your-email-address`por la dirección de correo.

### 3. Abrir una consola en el directorio del proyecto

Todos los comandos de git se escriben en una consola de comando. Para abrir una consola de comando en el directorio de nuestro proyecto debemos hacer **clic con el botón derecho** en el explorador y elegir la opción **Git Bash Here**.

<img src="img/git_bash_here.png" style="width: 80%; border: 1px solid #999; border-radius: 2px;">

### 4. Inicializar un repositorio local

Existen varias opciones para inicializar un repositorio. La que nos interesa ahora es crear un repositorio de git en una carpeta **donde ya existen nuestros archivos del proyecto**.

En la consola escribimos el siguiente comando:

```bash
git init .
```

Si todo sale bien veremos un mensaje como el siguiente.

<img src="img/git_init.png" style="width: 80%; border: 1px solid #999; border-radius: 2px;">



### 5. Consultando el estado actual del repositorio

Existen varias opciones para inicializar un repositorio. La que nos interesa ahora es crear un repositorio de git en una carpeta **donde ya existen nuestros archivos del proyecto**.

En la consola escribimos el siguiente comando:

```bash
git status
```

La salida debería ser algo similar a lo que se observa en la siguiente imagen.

<img src="img/git_status.png" style="width: 80%; border: 1px solid #999; border-radius: 2px;">

Git nos muestra en verde los archivos que estan agregados a la **fase de staging**, es decir los cambios marcados para ser archivados y en rojo los archivos que están aún fuera del control de cambios.

### 6. Agregando archivos a la fase de staging

Podemos imaginar a los **commits** como:

* una foto que sacamos de nuestro proyecto en un momento dado. 
* o una caja que contiene un montón de objetos que queremos guardar.

En ese sentido, la **fase de staging** sería el equivalente a ir poniendo en la caja los objetos que queremos guardar o ir pidiéndole a la gente que se forme y prepare para sacar la fotogragía.

<img src="https://miro.medium.com/max/700/1*ql265lWw8wu-vJbjbMvYGg.jpeg" style="width: 40%; border: 1px solid #999; border-radius: 2px;">

Para agregar archivos del proyecto a la fase de staging escribimos el comando `git add` seguido por el nombre de los archivos que queremos agregar, por ejemplo:

```bash
git add index.html
```

### 7. Realizando un commit

Si agregar archivos al **staging** fuera poner los objetos que queremos guardar dentro de una caja, **hacer un commit** sería como cerrar la caja con cinta y ponerle una etiqueta que dice lo que hay guardado dentro.

<img src="https://miro.medium.com/max/700/1*MCm2h0LIpfb1PjTp4Mds6w.jpeg" style="width: 40%; border: 1px solid #999; border-radius: 2px;">

Al hacer un commit se guarda el estado actual del proyecto. Esto permite hacer muchas cosas como rastrear los cambios del código entre diferentes commits, volver el proyecto a un punto anterior, etc.

Una vez que se agregaron todos los archivos relevantes a **staging**, se puede hacer un commit con el siguiente commando:

```bash
git commit -m "mensaje del commit"
```

Cada commit debe ir acompañado de un mensaje corto que describa en qué consisten los cambios que se almacenaron (la etiqueta de la caja).

### 8. Enviando los cambios a un servidor remoto

<img src="https://miro.medium.com/max/700/1*vkurnqLuLSWTuLok2rT07w.jpeg" style="width: 40%; border: 1px solid #999; border-radius: 2px;">

