# 1*4302?1
for i in range(10):
    d = int('1' + str(i) + '43021')
    if d % 3147 == 0:
        print(d)
for i in range(10):
    for j in range(0, 1000):
        d = int('1' + str(i) + '4302' + str(j) + '1')
        if d % 3147 == 0:
            print(d)