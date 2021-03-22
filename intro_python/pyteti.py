# -*- coding: utf-8 -*-
import os
import sys

##############################################
# VARIABLES
##############################################

# el tablero del juego
tablero = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# indica el jugador al que le toca (1 o 2)
jugador_turno = 1

# indica si hubo ganador:
# 1 para el jugador 1
# 2 para el jugador 2
# 0 si no hay ganador (empate)
ganador = 0

# cantidad de jugadas realizadas
cont_jugadas = 0

##############################################
# Procedimiento para dibujar el tablero
##############################################
def dibujar_tablero():
    for i in range(0, 3):
        print("+---+---+---+")
        for j in range(0, 3):
            c = " "
            if tablero[i][j] == 1:
                c = "o"
            elif tablero[i][j] == 2:
                c = "x"
            sys.stdout.write("| {} ".format(c))
        print("|")
    print("+---+---+---+")


##############################################
# Procedimiento para chequear el ganador
##############################################
def chequear_ganador():
    global ganador
    # Jugador 1
    # chequear si el jugador 1 hizo linea en la fila 0
    if tablero[0][0] == 1 and tablero[0][1] == 1 and tablero[0][2] == 1:
       ganador = 1

    ### TODO: chequear si el jugador 1 hizo linea en la fila 1
    ### TODO: chequear si el jugador 1 hizo linea en la fila 2

    # chequear si el jugador 1 hizo linea en la columna 0
    if tablero[0][0] == 1 and tablero[1][0] == 1 and tablero[2][0] == 1:
       ganador = 1

    ### TODO: chequear si el jugador 1 hizo linea en la columna 1
    ### TODO: chequear si el jugador 1 hizo linea en la columna 2

    # chequear si el jugador 1 hizo linea en la diagonal principal
    if tablero[0][0] == 1 and tablero[1][1] == 1 and tablero[2][2] == 1:
       ganador = 1

    ### TODO: chequear si el jugador 1 hizo linea en la diagonal secundaria

    # Jugador 2
    ### TODO: chequear si el jugador 2 hizo linea en la fila 0
    ### TODO: chequear si el jugador 2 hizo linea en la fila 1
    ### TODO: chequear si el jugador 2 hizo linea en la fila 2
    ### TODO: chequear si el jugador 2 hizo linea en la columna 0
    ### TODO: chequear si el jugador 2 hizo linea en la columna 1
    ### TODO: chequear si el jugador 2 hizo linea en la columna 2
    ### TODO: chequear si el jugador 1 hizo linea en la diagonal principal
    ### TODO: chequear si el jugador 1 hizo linea en la diagonal secundaria

##############################################
# El programa empieza aquí
##############################################
print("PY-TE-TI")
while cont_jugadas<6 and ganador == 0:
    dibujar_tablero()

    # si el usuario ingresa una posicion invalida
    # se le vuelve a solicitar que la ingrese (hasta que ingrese una valida)
    jugada_es_invalida = True
    while jugada_es_invalida:
        jugada_es_invalida = False
        print("Es el turno del jugador {}".format(jugador_turno))
        jugada_fila = int(input("Ingrese la fila: "))
        jugada_columna = int(input("Ingrese la columna: "))

        ### TODO: revisar que filas y columnas estén en el rango [0, 2]
        ### TODO: revisar que la posición del tablero este libre (en 0)
        ### TODO: si no es así: poner jugada_es_invalida = True para que vuelva a pedirla

        if jugada_es_invalida:
            print("ERROR: la posicion indicada no es válida, ingrese nuevamente")

    # aplica la jugada en el tablero
    tablero[jugada_fila][jugada_columna] = jugador_turno

    # cambia el turno
    if jugador_turno == 1:
        jugador_turno = 2
    else:
        jugador_turno = 1

    chequear_ganador()
    cont_jugadas = cont_jugadas + 1

# --- fin del while ---

# al finalizar dibujar la disposicion final del tablero
# y anunciar el ganador (o el empate)
dibujar_tablero()
if ganador == 1:
    print("GANO el jugador 1")
elif ganador == 2:
    print("GANO el jugador 2")
else:
    print("Hubo empate")
