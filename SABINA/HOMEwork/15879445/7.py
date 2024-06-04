from turtle import *
k=30
speed(450)
left(90)
right(45)
for i in range(7):
    forward(5*k)
    right(45)
    forward(10*k)
    right(135)
pu()
for x in range(0,15):
    for y in range(0,15):
        goto(x*k, y*k)
        dot(5)
done()