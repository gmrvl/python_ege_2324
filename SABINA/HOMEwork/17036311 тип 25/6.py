# 1?2711*0
for i in range(10):
    d = int('1' + str(i) + '27110')
    if d % 4891 == 0:
        print(d)
for i in range(10):
    for j in range(0, 1000):
        d = int('1' + str(i) + '2711' + str(j) + '0')
        if d % 4891 == 0:
            print(d)