from turtle import*
tracer(0)
left(90)
k = 20
for i in range(12):
    right(60)
    forward(1*k)
    right(60)
    forward(1*k)
    right(270)
pu()
for x in range(-3,5):
    for y in range(-7,1):
        goto(x*k,y*k)
        dot()
done()