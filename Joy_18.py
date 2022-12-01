from turtle import*
import colorsys

speed(0)
bgcolor('#252525')
h=0.3
for i in range(180):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    fd(i)
    rt(20)
    lt(80)
    circle(80-i)
done()
    