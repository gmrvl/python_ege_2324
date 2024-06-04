from turtle import *
k=40
speed(450)
left(90)
for i in range(5):
    forward(7*k)
    right(120)
pu()
for x in range(0,15):
    for y in range(0,15):
        goto(x*k, y*k)
        dot(5)
done()
