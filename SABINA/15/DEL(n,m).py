def f(x,a):
    return x % a == 0

a = 1          # а - натуральные, чтоб не начинать с нуля
while True:  # бесконечный цикл
    for x in range(1,100000):
        if not((not f (x,a)) <= (f(x,6) <= (not f(x,4)))):  # находим х, при котором нам А не подходит
            break
    else:  # если мы не брейкнулись, то идем в елз и А нам подходит
        print(a)
    a += 1

