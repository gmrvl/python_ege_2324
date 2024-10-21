from turtle import *
k=20
speed(450)
left(90)
for i in range(2):
    forward(21*k)
    right(90)
    forward(27*k)
    right(90)
up()
forward(9*k)
right(90)
forward(10*k)
left(90)
down()
for i in range(2):
    forward(86*k)
    right(90)
    forward(47*k)
    right(90)
pu()
for x in range(-10,15):
    for y in range(-10,15):
        goto(x*k, y*k)
        dot(5)
done()