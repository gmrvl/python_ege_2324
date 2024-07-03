from turtle import *
speed(150)
k = 30
left(90)
x = 1
forward((x+2)*k)

for i in range(4):
    forward(x * k)
    right(90)
    forward((x + 2)*k)

right(90)
forward((2*x)*k)
for i in range(4):
    right(90)
    forward((3*x - 1)*k)
for x in range(0, 15):
    for y in range(0, 15):
        goto(x*k, y*k)
        dot(5)
done()