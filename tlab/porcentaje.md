# Ejercicio

Se desea escribir un programa en C++ que se utilizará como parte de un software de asistencia para medición y evaluación de cultivos. Al comenzar el programa, el usuario ingresará un valor **N** que corresponde a la cantidad de plantas que fueron medidas. A continuación, el usuario deberá ingresar la altura de cada una de las N plantas. Se sabe que algunas plantas del cultivo fueron afectadas por una plaga que limitó su crecimiento y no superaron la altura de 0.5 metros. El programa debe **obtener e informar el porcentaje de plantas del cultivo que resultaron afectadas por la plaga** (es decir que no superaron los 0.5 metros de altura).

### Opcional

Mostrar la **altura promedio** de las plantas ingresadas, pero sin tener en cuenta las plantas afectadas por la plaga.

### Tips para tener en cuenta

* ¿Qué representa el valor N?

* ¿Cuántas alturas de plantas se van a ingresar?

* ¿Qué tipo de dato debería utilizar para almacenar la altura?

* El cálculo del porcentaje se puede hacer de la siguiente manera:

  ```porcentaje = &lt;cantidad&gt;/&lt;total&gt; * 100
  porcentaje = <cantidad_plantas_pequeñas>/<cantidad_total_plantas_ingresadas> * 100
  ```

* ¿El cálculo del porcentaje se debe realizar dentro o fuera del bucle? ¿Por qué?

