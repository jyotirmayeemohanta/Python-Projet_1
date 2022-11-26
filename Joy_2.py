from turtle import*

speed(0)
bgcolor('#252525')
c=['red','blue','purple','yellow','green']
pensize(2)
for i in range(200):
    color(c[i%5])
    fd(i)
    lt(100)
    fd(i)
    rt(160)
done()