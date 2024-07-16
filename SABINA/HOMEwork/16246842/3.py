for n in range(1, 10000):
    s = bin(n)[2:]
    s = s.replace('0', '*')
    s = s.replace('1', '0')
    s = s.replace('*', '1')
    while s[0] == '0' and len(s) > 1:
        s = s[1:]
    r = int(s, 2)
    r = n - r
    if r == 999:
        print(n)
