
for n in range(0,256):
    s = bin(n)[2:]
    while len(s) < 5:
        s = '0' + s
    s = s.replace('0', '*')
    s = s.replace('1', '0')
    s = s.replace('*', '1')
    s = int(s, 2)
    r = s - n
    if r == 133:
        print(n)


