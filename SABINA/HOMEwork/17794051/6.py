from turtle import*
speed(200)
k = 50
for i in range(4):
    forward(14*k)
    right(120)
pu()
for x in range(0,14):
    for y in range(-14,1):
        goto(x*k,y*k)
        dot()
done()