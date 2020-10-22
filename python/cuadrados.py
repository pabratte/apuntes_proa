import utils
import random

for i in range(500):
    x = random.randint(-200, 200)
    y = random.randint(-400, 400)
    ang = random.randint(0, 360)
    tam = random.randint(10, 50)
    color = (random.random(), random.random(), random.random())
    utils.cuadrado(x, y, ang, tam, color)

utils.guardar_imagen("cuadrados")