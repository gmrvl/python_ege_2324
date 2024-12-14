# 3?2258*4
for i in range(10):
    d = int('3' + str(i) + '22584')
    if d % 2024 == 0:
        print(d)
for i in range(10):
    for j in range(0, 1000):
        d = int('3' + str(i) + '2258' + str(j) + '4')
        if d % 2024 == 0:
            print(d)