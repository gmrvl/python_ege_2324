# 3*37*3?9
for i in range(10):
    d = int('3373' + str(i) + '9')
    if d % 9117 == 0:
        print(d)
for i in range(10):
    for j in range(0, 1000):
        d = int('3'+ str(j) + '373' + str(i) + '9')
        if d % 9117 == 0:
            print(d)
for i in range(10):
    for j in range(0, 1000):
        d = int('337'+str(j)+'3' + str(i) + '9')
        if d % 9117 == 0:
            print(d)
for i in range(10):
    for j in range(0, 1000):
            d = int('3'+str(j) + '37' +str(j)+'3' + str(i) + '9')
            if d % 9117 == 0:
                print(d)