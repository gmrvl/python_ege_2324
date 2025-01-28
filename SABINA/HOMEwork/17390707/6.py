from turtle import *
speed(100)
k = 20
for i in range(4):
    forward(k*14)
    right(90)
for i in range(5):
    forward(k*5)
    right(45)
pu()
for x in range(0,15):
    for y in range(0, -15, -1):
        goto(x*k,y*k)
        dot()
done()
