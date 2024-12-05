for n in range(0, 10000):
    bin_n = bin(n)[2:]
    if summ % 2 == 1:
        bin_n += '00'
    else:
        bin_n += '11'
    if r > 43:
        print(r)
        break
