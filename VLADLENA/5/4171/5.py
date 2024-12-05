for n in range(100, 1000):
    bin_n = bin(n)[2:]
    for i in range(3):
        nuli = bin_n.count('0')
        edinicy = bin_n.count('1')
        if nuli == edinicy:
            bin_n = bin_n + bin_n[-1]  # bin_n += bin_n[-1]
        elif nuli < edinicy:
            bin_n += '0'
        elif nuli > edinicy:
            bin_n += '1'
    r = int(bin_n, 2)
    if r % 4 == 0:
        print(n)
        break

