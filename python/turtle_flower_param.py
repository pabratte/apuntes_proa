import turtle
import random
import utils

def dibujar_cuadrado(tam, color):
    turtle.pencolor(color)
    for i in range(4):
        turtle.forward(tam)
        turtle.left(90)


def dibujar_petalos(color, tam, cant_petalos):
    angulo = 0
    for i in range(cant_petalos):
        dibujar_cuadrado(tam, color)
        turtle.left(360.0/cant_petalos)

def dibujar_hojas(tam_hoja):
    turtle.left(60)
    dibujar_cuadrado(tam_hoja+random.randint(-5, 5), "green")
    turtle.left(140)
    dibujar_cuadrado(tam_hoja+random.randint(-5, 5), "green")
    turtle.left(160)

def dibujar_tallo(largo_tallo):
    turtle.pencolor("green")
    turtle.left(90)
    turtle.forward(largo_tallo/2)
    dibujar_hojas(largo_tallo/10)
    turtle.forward(largo_tallo/2)

def dibujar_suelo(y):
    turtle.penup()
    turtle.goto(-400, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.pencolor("brown")
    turtle.forward(800)

def dibujar_flor(x, y, largo_tallo, tam, cant_petalos, color):
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    dibujar_tallo(largo_tallo)
    dibujar_petalos(color, tam, cant_petalos)



x = -300
y = -300
dibujar_suelo(y)
while x<300:
    # definir valores aleatorios para la flor
    largo_tallo = random.randint(50, 200)
    tam = random.randint(10, 40)
    cant_petalos = random.randint(5, 15)
    color = (1, random.random(), random.random())
    # dibujar
    dibujar_flor(x, y, largo_tallo,tam, cant_petalos, color)
    # adelantar x
    x = x + random.randint(30, 200)

utils.guardar_imagen("flores3")