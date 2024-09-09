from turtle import *
speed(100)
k = 20
left(90)
for i in range(9):
    forward(22*k)
    right(90)
    forward(6*k)
    right(90)
pu() #penup
forward(1*k)
right(90)
forward(5*k)
left(90)
pd() #pendown
for i in range(9):
    forward(53*k)
    right(90)
    forward(75*k)
    right(90)
pu()
for x in range(0,20):
    for y in range(0,20):
        goto(x*k,y*k)
        dot(5)
done()