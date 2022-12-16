import turtle as t
import colorsys as cs

t.setup(800,800)
t.speed(0)
t.width(2)
t.bgcolor('black')
t.seth(45)
n=180
for i in range(n):
    t.begin_fill()
    t.color(cs.hsv_to_rgb(i/6,i/n,0.8))
    t.fillcolor(cs.hsv_to_rgb(i/6,i/n,1))
    t.right(90)
    t.circle(i*1.2,90)
    t.end_fill()
    t.right(59)
t.hideturtle()
t.done()
    

        