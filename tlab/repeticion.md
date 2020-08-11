class: center, middle, inverse, layout
# Repetición en C++

## Taller Laboratorio

---

class: inverse
layout: true

---


# Repetición

Para **repetir** algo necesitamos:

* Una forma de **contar cuántas veces los hicimos**
* Saber si llegamos a la cantidad de veces que queríamos repetir

La computadora utiliza:
* Un contador
* Una condición

---

# Contador

Es una variable que **se incrementa** cada vez que pasa algo.

**Se incrementa** significa que *al valor que ya tenía* se le agrega algo más.


---


# Contador

Es una variable que **se incrementa** cada vez que pasa algo.

**Se incrementa** significa que *al valor que ya tenía* se le agrega algo más.

---

# Repetición con bucle for en C++

```
for(int cont=0; cont<5; cont++){
        cout<<"Hola"<<endl;
}
```
El programa muestra:
```
Hola
Hola
Hola
Hola
Hola
```
---

# Repetición con bucle for en C++

La variable **cont**, además de servir como contador para saber *cuándo* llegamos a las 5 vueltas, también se puede usar como valor dentro del bucle.

```
for(int cont=0; cont<5; cont++){
        cout<<"Repeti "<<cont<<" veces"<<endl;
}
```

El programa muestra:

```
Repeti 0 veces
Repeti 1 veces
Repeti 2 veces
Repeti 3 veces
Repeti 4 veces

```
---
# Ejercicios 

## Ejercicio 1
Escribir un programa que utilice un bucle for para mostrar por pantalla los números entre 0 y 30

## Ejercicio 2
Cómo modificaría el programa para que para que muestre por pantalla los valores entre 0 y un valor N ingresado por el usuario.




