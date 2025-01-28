from turtle import *
speed(1000)
k = 20
left(90)
for i in range(2):
    forward(9*k)
    right(90)
    forward(15*k)
    right(90)
pu()
forward(12*k)
right(90)
pd()
for i in range(2):
    forward(6*k)
    right(90)
    forward(12*k)
    right(90)
pu()
for x in range(0,10):
    for y in range(0,10):
        goto(x*k,y*k)
        dot()
done()
