from turtle import*
import colorsys

speed(0)
bgcolor('#252525')
h=0.7
for i in range(75):
    c=colorsys.hsv_to_rgb(h,1,1)
    fillcolor(c)
    h+=0.004
    begin_fill()
    rt(5)
    for j in range(4):
        fd(170)
        rt(90)
        end_fill()
done()
    