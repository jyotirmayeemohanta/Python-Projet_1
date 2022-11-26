from turtle import*
import colorsys as cs

speed(0)
bgcolor('#252525')
hideturtle()
pensize(4)
h=0.0
for i in range(180):
    c=cs.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    circle(190-i,100)
    lt(90)
    circle(190-i,100)
    rt(80)
done()
    
        
        