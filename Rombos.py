import turtle
import time

angulo = 45
lado = 100

turtle.left(200-angulo)
turtle.forward(lado)
turtle.right(90)
turtle.forward(lado)
turtle.right(90)
turtle.forward(lado)
turtle.right(90)
turtle.forward(lado)

longitud_linea = 5
espacio_linea = 2

turtle.right(160)
turtle.left(45)
for i in range(int(lado / (longitud_linea + espacio_linea))):
    turtle.forward(longitud_linea )
    turtle.penup()
    turtle.forward(espacio_linea)
    turtle.pendown()
turtle.right(90)
for i in range(int(lado / (longitud_linea + espacio_linea))):
    turtle.forward(longitud_linea )
    turtle.penup()
    turtle.forward(espacio_linea)
    turtle.pendown()
turtle.right(90)
for i in range(int(lado / (longitud_linea + espacio_linea))):
    turtle.forward(longitud_linea )
    turtle.penup()
    turtle.forward(espacio_linea)
    turtle.pendown()
turtle.right(90)
for i in range(int(lado / (longitud_linea + espacio_linea))):
    turtle.forward(longitud_linea )
    turtle.penup()
    turtle.forward(espacio_linea)
    turtle.pendown()

turtle.right(120)
turtle.forward(lado)
turtle.right(90)
turtle.forward(lado)
turtle.right(90)
turtle.forward(lado)
turtle.right(90)
turtle.forward(lado)
    
time.sleep(5)