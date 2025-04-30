from turtle import*
tracer(0)
k = 20
left(90)
for i in range(8):
    forward(6*k)
    right(120)
pu()
for x in range(0,7):
    for y in range(0,7):
        goto(x*k,y*k)
        dot()
done()
