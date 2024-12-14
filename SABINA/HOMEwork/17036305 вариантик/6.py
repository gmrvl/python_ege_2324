from turtle import*
speed(800)
k = 30
left(90)
for i in range(4):
    forward(k*6)
    right(150)
    forward(6*k)
    right(30)
pu()
for x in range(-7, 7):
    for y in range(-7, 7):
        goto(x*k, y*k)
        dot()
done()