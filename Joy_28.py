from turtle import*

speed(0)
bgcolor('#252525')
pensize(3)

for i in range(120):
    color("cyan")
    fd(i*2)
    lt(200)
    fd(i*2)
    rt(100)
    for j in range(2):
        rt(60)
done()