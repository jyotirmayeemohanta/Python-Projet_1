from turtle import*
import colorsys as cs

speed(0)
bgcolor('#252525')
pensize(2)
h=0.0
for i in range(300):
    c=cs.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    rt(i)
    circle(50,i)
    fd(i)
    lt(200)
done()
    