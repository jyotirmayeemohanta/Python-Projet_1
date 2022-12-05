import turtle as t
import colorsys as cs

t.speed(0)
t.tracer(7)
t.width(2)
t.bgcolor('#252525')
t.goto(0,-80)
def square(x):
    for i in range(4):
        t.fd(x)
        t.left(90)
h=0.0
for i in range(360):
    t.circle(80,1)
    t.right(90)
    t.color(cs.hsv_to_rgb(h,1,1))
    square(150)
    t.left(90)
    h+=0.003
t.hideturtle()
t.done()   