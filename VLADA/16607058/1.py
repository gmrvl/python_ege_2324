count = 0
for n in range(34722222, 45138888):
    bin_n = bin(n)[2:]
    ost = bin(n % 3)[2:]
    if len(ost) < 2:
        bin_n += '0'
    bin_n += ost
    ost2 = bin(int(bin_n, 2) % 5)[2:]
    if len(ost2) == 1:
        bin_n += '00'
    elif len(ost2) == 2:
        bin_n += '0'
    bin_n += ost2
    r = int(bin_n, 2)
    print(r)
    if 1111111110 <= r <= 1444444416:
        count += 1
print(count)
