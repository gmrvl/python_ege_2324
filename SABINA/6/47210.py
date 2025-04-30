from turtle import *
tracer(0) #если 0 мгновенно дает результат рисунка и точек
k = 30
left(90)
speed(100)
for i in range(7):
    forward(10*k)
    right(120)
pu()
for x in range(0, 15):
    for y in range(0, 15):
        goto(x*k, y*k)
        dot(5)
done()

