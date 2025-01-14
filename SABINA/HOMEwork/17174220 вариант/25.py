# 12??1*56
for i in range(10):
    for j in range(10):
        d = int('12'+ str(i)+str(j)+'156')
        if d % 317 == 0:
            print(d, d // 317)
for i in range(10):
    for j in range(0,10):
        for k in range(0, 10):
            d = int('12'+ str(i)+str(j)+'1'+ str(k)+ '56')
            if d <= (10**8) and d % 317 == 0:
                print(d, d // 317)
