for i in range(1, 10000):
    s = bin(i)[2:]
    s = s.replace('0', '*')
    s = s.replace('1', '0')
    s = s.replace('*', '1')
    while s[0] == 0:
        s = s[1:]
    r = int(s, 2)
    r = int(s) - int(r)
    if s == '999':
        print(r)
