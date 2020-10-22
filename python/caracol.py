import utils

# valores iniciales
angulo = 0
tam = 10
steps = 15
blue = 0
y = 0
x = 0

for i in range(steps):
    utils.cuadrado(x, y, angulo, tam, (1, 0, blue))
    tam = tam + 5
    angulo = angulo + 360.0/steps
    blue = blue + 1/steps
    #y = y - 5
    #x = x + 2

utils.guardar_imagen("caracol")
