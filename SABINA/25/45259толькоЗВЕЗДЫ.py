for i in range(10):
    for j in range(10):
        d = int('12345' + str(i) + '7' + str(j) + '8')
        if d % 23 == 0:
            print(d, d // 23)