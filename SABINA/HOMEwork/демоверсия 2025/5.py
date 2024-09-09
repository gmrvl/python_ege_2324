count = 0
for n in range(1,10000):
    s = bin(n)[2:]
    s = int(s)
    if s % 2 == 0 :
        s = '10' + str(s)
    else:
        s = '1' + str(s) + '01'
    r =int(s,2)
    if n < 13:
        print(r)