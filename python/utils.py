import turtle
from PIL import Image
import io
import os

def cuadrado(x, y, angulo, tam, color):
    # resetear el angulo y girar el indicado por el usuario
    turtle.setheading(0)
    turtle.left(angulo)
    # mover a la posicion
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    # dibujar el cuadrado
    turtle.pencolor(color)
    for i in range(4):
        turtle.forward(tam)
        turtle.left(90)

def guardar_imagen(nombre):
    turtle.hideturtle()
    cv = turtle.getcanvas()
    ps = cv.postscript(colormode='color')
    im = Image.open(io.BytesIO(ps.encode('utf-8')))
    filename = "{}/{}.png".format(os.path.dirname(os.path.abspath(__file__)), nombre)
    im.save(filename)
    print("Imagen guardada en: {}".format(filename))
    turtle.showturtle()