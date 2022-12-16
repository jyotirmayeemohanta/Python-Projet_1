import turtle as t
import colorsys as cs

t.setup(800,800)
t.tracer(10)
t.width(4)
t.bgcolor('#252525')
def square(x):
    for i in range(3):
        t.forward(x)
        t.left(90)
    t.forward(x)
for j in range(20):
    for i in range(10):
        t.color(cs.hsv_to_rgb(i/10,1-j/20,1))
        t.right(135)
        square(200-j*4)
        t.right(135)
        t.circle(50,36)
t.hideturtle()
t.done()