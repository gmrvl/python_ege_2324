from turtle import *
k = 50
goto(0,-7*k)
left(90)
speed(100)
for i in range(7):
    forward(10*k)
    right(120)
pu()
for x in range(-7, 15):
    for y in range(-7, 15):
        goto(x*k, y*k)
        dot(5)
done()
