from turtle import*
speed(500)
left(90)
k = 15
for i in range(5):
    forward(17*k) # отв 17
    right(90)
    forward(3*k)
pu()
for x in range(0,21):
    for y in range (-3, 18):
        goto(x*k,y*k)
        dot(5)
done()
