from turtle import *
k = 30
left(90)
speed(250)
for i in range(4):
    forward(9*k)
    right(90)
for i in range(3):
    forward(9*k)
    right(120)
pu()
for x in range(0,15):
    for y in range(0,15):
        goto(x*k, y*k)
        dot(5)
done()