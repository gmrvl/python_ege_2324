# 3?1*57
for i in range(10):
    d = int('3' + str(i) + '157')
    if d % 2023 == 0:
        print(d, d // 2023)
for i in range(10):
    for j in range(0, 1000):
        d = int('3' + str(i) + '1' + str(j) + '57')
        if d % 2023 == 0:
            print(d, d // 2023)