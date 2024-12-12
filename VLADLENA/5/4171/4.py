for n in range(0, 1000):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n = bin_n + '00'
    else:
        bin_n = bin_n + '11'
    r = int(bin_n, 2)
    if r < 94:
        print(n)