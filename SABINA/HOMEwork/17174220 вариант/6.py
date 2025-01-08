from turtle import*
speed(1000)
left(90)
k = 30
for i in range(3):
    forward(7*k)
    right(90)
forward(10*k)
for i in range(3):
    left(90)
    forward(6*k)
pu()
for x in range(-6,15):
    for y in range(-10,10):
        goto(x*k,y*k)
        dot()
done()