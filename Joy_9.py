from turtle import*

speed(0)
bgcolor('#252525')
color('cyan')

for i in range(110):
    for j in range(2):
        fd(i/7)
        circle(100,40)
        lt(20)
        circle(100,40)
    rt(120)
done()
