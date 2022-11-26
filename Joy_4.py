from turtle import*
import colorsys as cs

speed(0)
h= 0.2
bgcolor('#252525')

for i in range(170):
    c=cs.hsv_to_rgb(h,1,1)
    fillcolor(c)
    h+=0.02
    begin_fill()
    circle(190-i,90)
    lt(10)
    circle(190-i,90)
    lt(10)
    end_fill()
done()