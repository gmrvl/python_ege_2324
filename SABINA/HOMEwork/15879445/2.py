from turtle import *
k=30
left(90)
speed(300)
for i in range(3):
    forward(7*k)
    right(90)
forward(8*k)
for i in range(3):
    left(90)
    forward(5*k)
pu()
for x in range(-15,15):
    for y in range(-15,15):
        goto(x*k, y*k)
        dot(5)
done()
