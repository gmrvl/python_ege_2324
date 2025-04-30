from turtle import *
tracer(0) #если 0 мгновенно дает результат рисунка и точек
speed(100)
left(90)
k = 30
for i in range(4):
    forward(14*k)
    right(120)
pu()
for x in range(-14, 14):
    for y in range(-14, 14):
        goto(x*k, y*k)
        dot(5)
done()
