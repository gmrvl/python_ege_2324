from turtle import*
speed(100)
k = 35
for i in range(6):
    forward(13*k)
    right(120)
pu()
for x in range(0,14):
    for y in range(-13,1):
        goto(x*k,y*k)
        dot()
done()