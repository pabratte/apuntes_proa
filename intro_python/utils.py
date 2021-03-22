import turtle

def piernai():
    turtle.forward(50)

def cuerpo():
    turtle.left(90)
    turtle.forward(80)
    turtle.left(180)
    turtle.forward(170)
    turtle.left(180)
    turtle.forward(90)

def piernad():
    turtle.left(-90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(-90)
    turtle.forward(80)


def brazod():
    turtle.left(180)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(-90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(-90)


def atras():
    turtle.left(-90)
    turtle.forward(30)
    turtle.left(-90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)


def brazoi():
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(-90)
    turtle.forward(30)


def atras():
    turtle.left(180)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(-90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)

def cabeza():
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)

def muñeco():
    piernai()
    cuerpo()
    piernad()
    brazod()
    atras()
    brazoi()
    atras()
    cabeza()
muñeco()