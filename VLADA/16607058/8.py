count = 2
for n in range(987654321,2123456789):
    bin_n = bin(n)[2:]
    summ = bin_n.count('1')
    if summ % 2 == 1:
        bin_n += '1'
    else:
        bin_n += '0'
    r = int(bin_n, 2)
    print(r)