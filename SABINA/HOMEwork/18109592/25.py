for i in range(0,10):
    for i2 in range(0,10):
        s = '12'+ str(i) + str(i2) + '361'
        if int(s) % 273 == 0:
            print(s, int(s) / 273)
for i in range(0,10):
    for i2 in range(0,10):
        for j in range(0,10):
            s = '12' + str(i) + str(i2) + '36' + str(j) + '1'
            if int(s) % 273 == 0:
                print(s, int(s)/273)