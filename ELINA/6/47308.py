from turtle import *

right(90)
forward(10 * 30)
right(180)
#Повтори 5 [Вперёд 8 Направо 60 Вперёд 8 Направо 120]
for i in range(5):
    forward(8 * 30)
    right(60)
    forward(8 * 30)
    right(120)
up()

for x in range(0, 10):
    for y in range(-10, 10):
        goto(x * 30, y * 30)
        dot(5)
done()
