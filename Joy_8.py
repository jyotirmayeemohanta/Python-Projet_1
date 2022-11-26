from turtle import*
import colorsys as cs

speed(0)
bgcolor('#252525')
h=0.1

for i in range(110):
    c=cs.hsv_to_rgb(h,1,1)
    h+=0.004
    for j in range(2):
        fd(i/7)
        circle(100,40)
        lt(20)
        circle(100,40)
    rt(120)
done()
    