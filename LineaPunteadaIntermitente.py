import turtle
import time

longitud_linea = 5
espacio_linea = 2

for i in range(1, 10):
    turtle.forward(longitud_linea * i)
    turtle.penup()
    turtle.forward(espacio_linea)
    turtle.pendown()

time.sleep(5)