# 1?4*6?8
for i in range(10):
    d = int('1' + str(i) + '46'+ str(i)+ '8')
    if d % 2622 == 0:
        print(d, d // 2622)
for i in range(10):
    for j in range(0, 1000):
        d = int('1' + str(i) + '4' + str(j) +'6'+ str(i) + '8')
        if d % 2622 == 0:
            print(d, d // 2622)