#1
'''from turtle import *
for i in range (5):
    forward (7)
    right (90)
    forward (4)
    right (90)'''
 #2
'''from turtle import *
for i in range (2):
    forward (10)
    right (90)
    forward (18)
    right (90)
up()
forward (5)
right (90)
forward (7)
left (90)
down ()
for i in range (2):
    forward (10)
    right (90)
    forward (7)
    right (90)'''
#3
'''from turtle import *
for i in range (5):
    forward (5*30)
    right (120)
    done ()'''
#4
'''from turtle import *
for i in range (6):
    forward (13*30)
    right (120)
    done ()'''
#5
'''from turtle import *
for i in range (4):
    forward (8*30)
    right (90)
    forward (8*30)
    right (90)
    dot ()
    done ()'''
#6
'''from turtle import *
for i in range (4):
    forward (5*30)
    right (90)
    forward (7*30)
    right (90)
    done ()'''
#7
'''from turtle import *
for i in range (8):
    forward (6*30)
    right (120)
    done ()'''
#8
'''from turtle import *
for i in range (4):
    forward (8*30)
    right (90)
for i in range (3):
    forward (12*30)
    right (120)
    done ()'''
#9
'''from turtle import *
left (90)
forward (100)
right (90)
for i in range (2):
    forward (9*30)
    right (90)
    forward (15*30)
    right (90)
up()
forward (12*30)
right (90)
down()
for i in range (2):
    forward (6*30)
    right (90)
    forward (12*30)
    right (90)
done ()'''
#10
'''from turtle import *
for i in range (4):
    forward (120)
    right (90)
for i in range (3):
    forward (120)
    right (120)
done ()'''
#11
'''from turtle import *
for i in range (6):
    forward (70)
    right (90)
    forward (70)
    right (90)
done ()'''
#вариант егэ
'''from turtle import *
for i in range (8):
    forward (60)
    right (120)
    done ()'''
from turtle import *
for i in range (2):
    forward (30)
    left (90)
    back (100)
    left (90)
up()
back (100)
right (90)
forward (80)
left (90)
down()
for x in range (2):
    forward (160)
    right (90)
    forward (80)
    right (90)
up()
for x in range(-10, 10):
    for y in range(-15, 0):
        goto(x * 10, y * 10)
        dot(5)
done()