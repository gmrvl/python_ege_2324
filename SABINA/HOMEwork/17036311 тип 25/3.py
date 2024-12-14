# 1*4022?9
for i in range(10):
    d = int('1' + str(i) + '40229')
    if d % 1987 == 0:
        print(d)
for i in range(10):
    for j in range(0, 1000):
        d = int('1' + str(i) + '4022' + str(j) + '9')
        if d % 1987 == 0:
            print(d)