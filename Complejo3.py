import turtle as t
import math

x = -2*(math.pi)
A = 100
B = 100
C = 0
D = 0

period = (2*(math.pi)/B)

Y = A*(math.sin((period*x-C)+D))
t.penup()
t.goto(x,Y)
t.pendown()

x = (-23*(math.pi)/12)
while x!= 2*(math.pi):
    Y = A*(math.sin((period*x-C)+D))
    t.goto(x,Y)
    x = x+((math.pi)/12)