
import turtle
colores=(str(input("ingrese color ")))
def dibujar_cuad():
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)

def dibujar_roseton():
        for i in range(20):

            turtle.left(36)
            turtle.color(colores)
            dibujar_cuad()


        for i in range(20):
            turtle.left(28)
            turtle.color('pink')
            dibujar_cuad()
def dibujar_palo():
        turtle.color('green')
        turtle.right(90)
        turtle.forward(100)
        turtle.forward(100)

def dibujar_rosetonn():
        dibujar_roseton()
        dibujar_palo ()


for i in range(11):
    dibujar_rosetonn ()