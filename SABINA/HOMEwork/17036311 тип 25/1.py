# 1?2139*4
for i in range(10):
    m = int('1' + str(i) + '21394')
    if m % 2023 == 0:
        print(m, m//2023)
for i in range(10):
    for j in range(0,1000):
        m = int('1' + str(i) + '2139' + str(j) + '4')
        if m % 2023 == 0:
            print(m, m//2023)
