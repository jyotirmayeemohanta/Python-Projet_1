from turtle import*
import colorsys

speed(0)
bgcolor('#252525')
h=0.0
pensize(2)
for i in range(390):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    fd(i)
    lt(100*2)
    rt(20)
    lt(5)
done()
    