from turtle import *
speed(300)
k = 50
left(90)
for i in range(4):
    forward(6*k)
    right(150)
    forward(6*k)
    right(30)
pu()
for x in range(-9,9):
    for y in range(-9,9):
        goto(x*k,y*k)
        dot()
done()
