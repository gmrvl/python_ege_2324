from turtle import *
k = 30

speed(100)
for i in range(6):
    forward(7 * k)
    right(90)
    forward(7 * k)
    right(90)
pu()
for x in range(0, 7):
    for y in range(-7, 1):
        goto(x*k, y*k)
        dot(5)
done()
#64
