class: center, middle, inverse, layout
# Listas y diccionarios en Python

## Programación I

### The Movie Database
---

class: inverse
layout: true

---

# Listas y diccionarios aplicados a un caso real

## The Movie Data Base

<div style="text-align: center;">
  <img src="img/tmdb.png" style="width: 60%;">
</div>

* Es un sitio con datos sobre películas
* Tiene una API (Application Programming Interface), es decir, un interfaz que permite acceder a los datos de manera unificada desde diferentes lenguajes/aplicaciones
* Vamos a visualizar y filtrar los datos utilizando Python

---


## The Movie Data Base en Python

* Vamos a utilizar una biblioteca llamada [tmdbsimple](https://pypi.org/project/tmdbsimple/)


---


## Instalar bibliotecas en Python

Utilizamos el gestor de paquetes de Python: pip

<div style="text-align: center;">
  <img src="img/pip.png" style="width: 60%;">
</div>

1. Abrimos Mu-editor
2. Hacemos clic en el botón REPL
3. En la consola de abajo escribimos
```
pip install tmdbsimple
```

---

## Ejemplo básico utilizando tmdbsimple

Muestra *los títulos* de las películas que tengan *twilight* en el nombre.

```python
import tmdbsimple as tmdb
tmdb.API_KEY = '170674ae8ffcffc07aa4bddd494866e2'

search = tmdb.Search()
search.movie(query='twilight')

for movie in search.results:
    print(movie['title'])
```


---

## ¿Cómo funciona?

```python
# importa la biblioteca
import tmdbsimple as tmdb

# configura la credencial para conectarnos                 
tmdb.API_KEY = '170674ae8ffcffc07aa4bddd494866e2'

# crea un objeto (variable) para realizar la busqueda
search = tmdb.Search()

# realiza la búsqueda
search.movie(query='twilight')

# recorre los resultados
for movie in search.results:
    print(movie['title'])
```

---


## ¿Cómo funciona?

```python
search.movie(query='twilight')
```

* Devuelve una lista de elementos
* Cada elemento de la lista es un diccionario

```python
{
    'popularity': 51.401,
    'vote_count': 17188,
    'video': False,
    'poster_path': '/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg',
    'id': 603,
    'adult': False,
    'backdrop_path': '/ByDf0zjLSumz1MP1cDEo2JWVtU.jpg',
    'original_language': 'en',
    'original_title': 'The Matrix',
    'genre_ids': [28, 878],
    'title': 'The Matrix',
    'vote_average': 8.1,
    'overview': 'Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.',
    'release_date': '1999-03-30'
}
```
---


## ¿Cómo funciona?

Una lista, donde cada elemento (película) es un diccionario

```python
search.results = [ 
  {
      'popularity': 51.401,
      'vote_count': 17188,
      ...
  },
  {
      'popularity': 51.401,
      'vote_count': 17188,
      ...
  },
  {
      'popularity': 51.401,
      'vote_count': 17188,
      ...
  }
]
```
---

## Otro ejemplo

Lista el *título*, *fecha de estreno* y *popularidad* de todas las películas que coincidan con "anabele"

```python
import tmdbsimple as tmdb
tmdb.API_KEY = '170674ae8ffcffc07aa4bddd494866e2'

search = tmdb.Search()
search.movie(query='anabele')

for movie in search.results:
    print("{} {} {}".format(movie['title'], movie['release_date'], movie['popularity']))

```
```
Elvis and Anabelle 2007-03-10 7.086
Killing Anabella  0.6
Anabelle Huggins Story: Ruben Ablaza Tragedy - Mea Culpa 1995-01-04 0.84
Annabelle Comes Home 2019-06-26 22.747
Annabelle 2014-10-02 15.62
Annabelle: Creation 2017-08-03 25.554
```
---

# ¡A obtener y manipular datos!


---
## Ejercicios 
Obtener los siguientes resultados (puede ser todo en un mismo archivo o archivos separados)

1. Listar los **títulos** (title) de las películas que coincidan con un *término de búsqueda ingresado por el usuario*.

2. Mostrar **título** y **cantidad de votos** (vote_count) *sólo para el primer resultado* de la búsqueda de películas de *"Harry Potter"*.

3. Mostrar **fecha de lanzamiento** (release_date), **puntaje promedio** (vote_average) y **título** (title) de las *películas de Transformers* cuyo *puntaje promedio sea mayor o igual a 6.5*.

4. Mostrar el **resumen** (overview) de la pelicula *Matrix Revolutions* (cuidado con la cantidad de resultados).

5. Mostrar el **título** (title) de la película con **puntaje promedio** (vote_average) **más alto** correspondiente a la saga "Hunger Games" (Los Juegos del Hambre).
