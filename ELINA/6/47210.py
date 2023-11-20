count = 0
for x in range(1, 10):
    for y in range(1, 10):
        # если точки на линии учитывать нужно, то range(0, n+1)
        # тут пишется уравнение для фигуры!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if -x / 3 ** 0.5 + 10 > y > x / 3 ** 0.5:
            count += 1
print(count)

# как нарисовать фигуру

# from turtle import *
# left(90)
# for i in range(7):
#     forward(10 * 30)
#     right(120)
# done()
