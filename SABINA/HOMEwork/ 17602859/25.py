#1?2139*4
for i in range(10):
    d = int('1' + str(i) + '21394')
    if d % 2023 == 0:
        print(d, d // 2023)
for i in range(10):
    for j in range(0, 1000):
        d = int('1' + str(i) + '2139' + str(j) + '4')
        if d % 2023 == 0:
            print(d, d // 2023)