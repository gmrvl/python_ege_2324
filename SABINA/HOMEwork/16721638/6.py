from turtle import*
speed(500)
left(90)
k = 20
for i in range(6):
    forward(2*k)
    right(90)
    forward(7*k)
pu()
for x in range(0,10):
    for y in range(-7,3):
        goto(x*k,y*k)
        dot()
done()
