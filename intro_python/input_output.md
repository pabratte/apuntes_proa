
# Entrada y salida en Python

## Entrada

Para ingresar valores por consola en Python 3 se utiliza la función *input()*. Por ejemplo:

```
a = input()
```

También se puede especificar como argumento de input un texto que se mostrará al usuario. Por ejemplo:

```
a = input("Ingrese algo: ")
```

**Muy importante**: en Python 3 la función *input()* devuelve lo que ingresó el usuario pero con el tipo *str* (ya que lo que el usuario ingresa desde la consola es, técnicamente, texto). Por lo tanto, si queremos leer un valor entero, deberemos aplicar una conversión explícita a lo que el usuario ingresó antes de almacenarlo en la variable, por ejemplo:

```
a = int(input("Ingrese un entero: "))
```

ó, en más pasos

```
b = input("Ingrese un entero: ")
a = int(b)
```

## Salida

En Python 3 la salida por consola se realiza mediante la función *print()*, pasando dentro de los paréntesis. Por ejemplo:

```
print("Hola!!!")
a = 5
print(a)
```

### Strings con formato

Ver [éste artículo](https://realpython.com/python-f-strings/)

#### Forma vieja (%)

```
>>> print('El valor de pi es aproximadamente %f.' % (3.142))
El valor de pi es aproximadamente 3.142.
```

#### Forma nueva (format)

``` 
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```
