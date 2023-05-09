import turtle
import math
import time

lado = 100
diagonal = math.sqrt(lado ** 2 + lado ** 2)

turtle.right(180)
turtle.left(45)
turtle.forward(lado)
turtle.right(90)
turtle.forward(lado)
turtle.right(90)
turtle.forward(lado)
turtle.right(90)
turtle.forward(lado)
turtle.right(135)
turtle.forward(diagonal)
turtle.left(90)
turtle.forward(diagonal)
turtle.left(135)
turtle.forward(lado * 2)
turtle.right(135)
turtle.forward(diagonal)
turtle.right(135)
turtle.forward(lado)
turtle.left(90)
turtle.forward(lado)
turtle.left(135)
turtle.forward(diagonal)
time.sleep(5)