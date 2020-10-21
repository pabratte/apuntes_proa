# Repetición simple vs repetición condicional en C++

## Repetición Simple

* Sabemos de antemano cuántas veces vamos a repetir.
* **Utilizamos un bucle con contador**.

```c++
for(int i=0; i<10; i++){
	...
}
```

```c++
int cont = 0;
while(cont<10){
	...
	cont++;
}
```

## Repetición Condicional

* **NO** sabemos de antemano cuántas veces vamos a repetir.
* **No podemos utilizar un contador** (no podemos usar un bucle for).
* Utilizamos un bucle while.


Ejemplo, ingresar valores hasta que el usuario ingrese 0.
```c++
int valor;
cin>>valor;
while(valor != 0){
	...
	cin>>valor;
}
```

## Ejemplo

Escribir un programa que permita calcular **la suma de una serie de números enteros** ingresados por el usuario. **Se desconoce de antemano cuántos valores se van a ingresar**, pero se sabe que el ingreso de datos termina cuando el usuario ingresa el valor 0.

* ¿Cómo resolveríamos el problema si supieramos que se van a ingresar sólo 10 datos?
* ¿Qué cambia en el caso de repetición condicional?


## Actividades

* Resolver el siguiente ejercicio en C++ y subir la solución al buzón.


En una fábrica se elaboran caramelos masticables de distintos gustos (frutilla, naranja, manzana y uva), que se distribuyen en bolsas de distintos tamaños (50, 100 y 150 caramelos). Cada bolsa posee caramelos de un único gusto. A partir de las bolsas elaboradas en un día, se desea conocer cuántos caramelos en total se fabricaron de cada gusto. Se necesita crear un programa en el que se ingrese como datos el gusto y el tamaño (cantidad de caramelos) de una serie de bolsas. Se necesita conocer la cantidad de caramelos en total de cada gusto (tener en cuenta que cada bolsa puede tener 50, 100 o 150 caramelos). Se desconoce de antemano la cantidad de bolsas que se ingresarán, pero se sabe que el programa termina cuando se ingresa 0 como cantidad de caramelos en la bolsa.


