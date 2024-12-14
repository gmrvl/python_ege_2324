# 1?954*21
for i in range(10):
    d = int('1' + str(i) + '95421')
    if d % 3023 == 0:
        print(d)
for i in range(10):
    for j in range(0, 1000):
        d = int('1' + str(i) + '954' + str(j) + '21')
        if d % 3023 == 0:
            print(d)