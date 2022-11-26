from turtle import *

bgcolor('black')
speed(0)
setup(500,500)
pensize(2)
pencolor('indigo')

for i in range(9):
    right(180)
    forward(50)
    for j in range(100):
        pendown()
        forward(100)
        right(65)
hideturtle()
exitonclick()