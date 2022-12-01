from turtle import*
import colorsys

speed(0)
bgcolor('#252525')
h=0.8
pensize(3)
for i in range(60):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.1
    fd(i)
    rt(20)
    circle(150)
    lt(20)
    rt(40)
done()