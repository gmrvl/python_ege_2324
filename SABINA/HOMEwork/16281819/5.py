for n in range(0, 256):
    s = bin(n)[2:]
    print(s)
#    print('stp')
    s = s.replace('0', '*')
    s = s.replace('1', '0')
    s = s.replace('*', '1')
#    print(s)
    s = int(s, 2)
    r = n - s
    if r == 133:
        print(n)
