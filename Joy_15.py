from turtle import*
import colorsys as cs

speed(0)
h=0.2
bgcolor('#252525')
pensize(3)

for i in range(300):
    c=cs.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.002
    fd(i)
    circle(20,70)
    if i%3==0:
        circle(200,70)
done()