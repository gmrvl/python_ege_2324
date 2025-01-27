#1*4022?9
for i in range(10):
    d = int('14022'+ str(i)+'9')
    if d % 1987 == 0:
        print(d)
for i in range(10):
    for j in range(100):
        d = int('1'+str(j)+'4022'+ str(i)+ '9')
        if d % 1987 == 0:
            print(d)