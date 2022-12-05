from turtle import*
import colorsys

speed(0)
bgcolor('#252525')
pensize(3)
h=0.7
for i in range(60):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    fd(i)
    rt(20)
    circle(150)
    lt(20)
    rt(40)
done()
    