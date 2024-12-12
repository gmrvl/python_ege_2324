a = []
for n in range(0, 10000):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n = '1' + bin_n + '0'
    else:
        bin_n = '11' + bin_n + '11'
    r = int(bin_n, 2)
    if r > 52:
        a.append(r)
print(min(a))

