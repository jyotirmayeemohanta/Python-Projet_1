from turtle import*
import colorsys as cs

speed(0)
h=0.1
bgcolor('#252525')
pensize(2)
for i in range(200):
    c=cs.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    for i in range(4):
        fd(i/7)
        circle(100,40)
        lt(20)
        circle(100,40)
    rt(120)
done()   