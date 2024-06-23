from turtle import *
k = 30 #коэффициент для увеличения масштаба
left(90)
speed(20)

for i in range(5):
    seth(0)
    circle(5*k,180)
    seth(90)
    circle(5*k,180)
    seth(180)
    circle(5*k,180)
    seth(270)
    circle(5*k,180)
pu()
for x in range(-15,6,1):
    for y in range(-5,16):
        goto(x*k , y*k )
        dot(5)
pu()
done()