for n in range(0, 10000):
    bin_n = bin(n)[2:]
    if n % 2 == 1:
        bin_n += '11'
    else:
        bin_n += '00'
    r = int(bin_n, 2)
    if r <= 94:
        print(n)
