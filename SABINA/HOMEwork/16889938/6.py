from turtle import*
speed(0)
left(90)
k = 35
for i in range(8):
    right(45)
    forward(k*6)
pu()
for x in range(0, 16):
    for y in range(-11,6):
        speed(0)
        goto(x*k,y*k)
        dot()
done()