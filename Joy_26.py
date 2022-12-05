from turtle import*
import colorsys

speed(0)
bgcolor('#252525')
pensize(2)
h=0
for i in range(445):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    circle(190-i,30)
    rt(20)
    lt(220)
    circle(190-i,30)
done()