from turtle import*
import colorsys as cs

speed(0)
bgcolor('#252525')
pensize(2)
h=0.2
for i in range(400):
    c=cs.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    circle(i-100,80)
    lt(100)
    circle(i-100,80)
done()