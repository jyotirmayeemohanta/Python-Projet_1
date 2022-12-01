from turtle import*
import colorsys

speed(0)
bgcolor('#252525')
h=0.8
pensize(3)
for i in range(80):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    for j in  range(17):
        fd(0.2*i*j)
        lt(33/0.01)
done()
