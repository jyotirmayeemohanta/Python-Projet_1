import turtle as t
import colorsys as cs
t.bgcolor('black')
t.tracer(10)
t.width(2)
def squaare(x):
    for i in range(3):
        t.forward(x)
        t.left(90)
    t.forward(x)
n = 35
for i in range(n):
    t.color(cs.hsv_to_rgb(1-i/n,1-i/n,1))
    for j in range(4):
        squaare(30+(i*3))
        t.circle(30+(i*3))
t.hideturtle()
t.done()
            