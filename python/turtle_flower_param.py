
import turtle
import random


def cuadrado(x, y, tam, angulo, col):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(col)
    turtle.left(angulo)
    # dibujar el cuadrado
    for i in range(4):
        turtle.forward(tam)
        turtle.left(90)
        turtle.circle(90)

def dibujar_tallo(largo_tallo, x,ang):
    turtle.pencolor("green")
    turtle.left(90)
    turtle.forward(largo_tallo/2)
    turtle.forward(largo_tallo/2)
    turtle.penup()
    turtle.goto(x, -100)
    turtle.pendown()
    turtle.left(ang)


def dibujar_suelo(y):
    turtle.penup()
    turtle.goto(-400, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.pencolor("brown")
    turtle.forward(800)

cuadrado(100, 200, 20,random.randint(0, 360),(random.random(), random.random(), random.random()))
cuadrado(200, 100, 10,random.randint(0, 360),(random.random(), random.random(), random.random()))
xx = 0
yy = -100
cuadrado(xx, yy, 30,random.randint(0, 360),(random.random(), random.random(), random.random()))
dibujar_suelo(yy)
dibujar_tallo(200,300,270)
dibujar_tallo(200,200,270)
dibujar_tallo(200,100,270)
dibujar_tallo(200,0,270)
dibujar_tallo(200,-100,270)
dibujar_tallo(200,-200,270)
dibujar_tallo(200,-300, 270)
dibujar_tallo(200,-400, 270)
dibujar_tallo(200,-500, 0)