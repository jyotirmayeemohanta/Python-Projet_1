from turtle import*
import colorsys as cs

speed(0)
bgcolor('#252525')
pensize(3)
h=0.0

for i in range(100):
    c=cs.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    for j in range(2):
        fd(i)
        rt(60)
        fd(300)
        rt(120)
    rt(60*2+1)
done()