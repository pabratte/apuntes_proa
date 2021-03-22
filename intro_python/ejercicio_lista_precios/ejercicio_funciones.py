# -*- coding: utf-8 -*-
# TODO #1a: importar  el modulo db_productos

productos = []
# TODO #1b: cargar la lista de productos con la función
#          cargar_productos() del módulo db_productos.

# TODO #2: definir una función mostrar_productos()
#          que reciba la lista de productos, no retorne nada,
#          y muestre la lista utilizando el siguiente formato para cada producto:
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# ...

# TODO #3: definir una función calcular_precio_actualizado()
#          que reciba: el precio anterior y porcentaje de aumento
#          y retorne: el precio con el aumento.

# TODO #4: Crear una función actualizar_precios() que reciba la lista de productos y 
#          el porcentaje de aumento. La función debe recorrer cada producto de la
#          lista e invocar calcular_precio_actualizado() (a la cual tendrá que pasarle
#          el precio del producto y el porcentaje de aumento) para obtener el precio
#          actualizado y modifique la lista "in-place" actualizando el precio de cada
#          producto. La función no debe retornar nada sino dejar modificada la lista
#          pasada por el usuario.

if __name__ == '__main__':
    # TODO #5a: mostrar la lista cargada
    # TODO #5b: el usuario debe ingresar el porcentaje de aumento
    # TODO #5c: usar la función actualizar_precios() para actualizar los precios de la lista
    # TODO #5d: mostrar la lista con los precios actualizados