from turtle import *
k=20
speed(450)
left(90)
right(60)
for i in range(2):
    forward(10*k)
    right(120)
    forward(5*k)
    right(240)
right(120)
forward(3*k)
right(90)
forward(20*(3 ** 0.5))
right(90)
forward(8*k)
right(120)
for i in range(2):
    forward(10*k)
    right(120)
    forward(5*k)
    left(240)
pu()
for x in range(-5,35):
    for y in range(-5,15):
        goto(x*k, y*k)
        dot(5)
done()