from turtle import *
speed(500)
left(90)
k = 29
for i in range(4):
    forward(10*k)
    right(60)
    forward(10*k)
    right(120)
pu()
for x in range(-9, 17):
    for y in range(-9,17):
        goto(x*k, y*k)
        dot()
done()