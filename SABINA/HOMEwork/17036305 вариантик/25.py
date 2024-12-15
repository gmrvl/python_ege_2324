# 1?2655*8
for i in range(10):
    d = int('1' + str(i) + '26558')
    if d % 4173 == 0:
        print(d)
for i in range(10):
    for j in range(0, 1000):
        d = int('1' + str(i) + '2655' + str(j) + '8')
        if d % 4173 == 0:
            print(d)
        d = int('1' + str(i) + '26550' + str(j) + '8')
        if d % 4173 == 0 and d < 10**10:
            print(d)
        d = int('1' + str(i) + '265500' + str(j) + '8')
        if d % 4173 == 0 and d < 10**10:
            print(d)
