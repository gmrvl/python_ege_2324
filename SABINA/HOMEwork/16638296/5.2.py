for i in range( 1000, 10000):
    s = str(i)
    a1 = s[0]
    a2 = s[1]
    a3 = s[2]
    a4 = s[3]
    summ1 = int(a1) + int(a2)
    summ2 = int(a2) + int(a3)
    summ3 = int(a3) + int(a4)
    sr = summ1 + summ2 + summ3 - max(summ1, summ2 , summ3) - min(summ1, summ2 , summ3)
    #print(sr)
    r =  str(sr) + str(max(summ1, summ2 , summ3))
    #print(r)
    if r == '1517':
        print(i)