from turtle import*

speed(0)
bgcolor('#252525')
c = ('red','green','blue')
for i in range(120):
    color(c[i%3])
    begin_fill()
    fd(i*2)
    lt(200)
    fd(i*2)
    rt(100)
    for j in range(2):
        rt(60)
        end_fill()
done()
        