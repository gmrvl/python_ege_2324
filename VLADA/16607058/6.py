for n in range (0, 10000):
    bin_n = bin (n)[2:]
    summ = bin_n.count('1')
    if summ % 2 ==1:
        bin_n += '10'
    else:
        bin_n += '00'
    r= int (bin_n,2)
    if r> 396:
        print (r)
        break