import turtle as t
import colorsys as cs

t.speed(0)
t.width(2)
t.bgcolor('#252525')
for i in range(300):
    t.color(cs.hsv_to_rgb(i/300,0.5,1))
    t.forward(i)
    t.left(59)
t.hideturtle()
t.done()