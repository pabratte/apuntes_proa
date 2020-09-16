# ¿Qué hace el siguiente código?

Analizar qué es lo que hace el siguiente código:

```
#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
	string a;
	float b;
	
	int cont_1 = 0;
	int cont_2 = 0;
	
	for(int i=0; i<10; i++) { 
		cin>>a;
		cin>>b;
		if(b > 3.5){
			if(a == "blanco"){
				cont_1++;
			}else if(a == "negro"){
				cont_2++;
			}
		}
	}
	
	cout<<cont_1<<endl;
	cout<<cont_2<<endl;
	
	return 0;
}
```

Por supuesto, sin conocer la situación problemática que resuelve es un poco difícil saber qué es lo que hace, pero de todas maneras podemos analizar las variables, sus relaciones, las condiciones, etc.

Algunas preguntas que nos podemos plantear para su funcionamiento son:

* ¿Cuáles son las variables que intervienen?¿Qué función cumple cada una? Por ejemplo: ¿las ingresa el usuario?¿en qué parte del programa aparecen?¿qué operaciones se hacen con ellas?
* ¿Cuántos datos ingresa el usuario?¿De qué tipo?
* ¿Cuál cree que será la salida del programa?


## Actividades

1. **Grabar un audio** de entre 30 segundos y un minuto donde explique con sus palabras qué es lo que hace el código. Para grabar el audio se sugiere utilizar la herramienta [Vocaroo](https://vocaroo.com/). Luego de grabar el audio puede descargarlo o copiar el link.

2. **Inventar y escribir** el enunciado de una situación problemática que se resuelva utilizando el código del ejemplo. Debe contener, por lo menos, las siguientes partes:
	* **Contexto o descripción de la situación problemática**: ¿de qué trata?¿juguetes?¿estudiantes?¿alturas de plantas? Debe explicar por qué es necesario un programa para resolverlo
	* **Entrada**: ¿qué es lo que va a ingresar el usuario?
	* **Salida**: ¿qué representan los datos de salida que mostrará el programa?
	
## Entrega

Subir al buzón de la tarea:
* El archivo de audio (o un enlace)
* Un texto en Word/Notepad/etc con el enunciado de la situación problemática
* Pueden trabajar de manera individual o en grupos de 2, con los mismos compañeros que venían trabajando
* No se aceptarán enunciados copiados o repetidos



