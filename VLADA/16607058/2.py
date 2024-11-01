for n in range(432101, 0, -1):
    bin_n = bin(n)[2:]
    if n % 5 == 0:
        bin_n += bin(5)[2:]
    else:
        bin_n += '1'
    if int(bin_n, 2) % 7 == 0:
        bin_n += bin(7)[2:]
    else:
        bin_n += '1'
    r = int(bin_n, 2)
    if r < 1728404:
        print(n)
        break



