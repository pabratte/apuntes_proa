import turtle

# definir el procedimiento
def dibujar_cuadrado():
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)

def dibujar_petalos():
    for i in range(10):
        turtle.left(36)
        dibujar_cuadrado()

def dibujar_hojas():
    turtle.left(60)
    dibujar_cuadrado()
    turtle.left(140)
    dibujar_cuadrado()
    turtle.left(160)

def dibujar_tallo():
    turtle.right(90)
    turtle.forward(100)
    dibujar_hojas()
    turtle.forward(100)

def dibujar_suelo():
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(200)

def dibujar_flor():
    dibujar_petalos()
    dibujar_tallo()
    dibujar_suelo()

dibujar_flor()