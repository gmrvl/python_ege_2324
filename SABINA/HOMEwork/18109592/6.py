from turtle import*
speed(100)
k = 20
for i in range(8):
    forward(6*k)
    right(120)
pu()
for x in range(0,7):
    for y in range(-6,1):
        goto(x*k,y*k)
        dot()
done()
