import turtle
import time

# turtle.backward(100)
# turtle.right(100)
# turtle.left(100)
# turtle.sety(50)
# turtle.setx(200)
# turtle.sety(-15)
# turtle.setx(-20)
# turtle.circle(100)
# turtle.penup()
# turtle.pendown()

lado1 = 100
lado2 = 50
turtle.left(90)
turtle.forward(lado2)
turtle.right(90)
turtle.forward(lado1)
turtle.right(90)
turtle.forward(lado2)
turtle.left(90)
turtle.backward(lado1)
time.sleep(5)