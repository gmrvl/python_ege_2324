for n in range(0, 1000):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n = bin_n + '10'
    else:
        bin_n = bin_n + '01'
    r = int(bin_n, 2)
    if r <= 102:
        print(r)
