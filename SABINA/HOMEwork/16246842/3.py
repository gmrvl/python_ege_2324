for i in range(1,10000):
    s = bin(i)[2:]
    while '0' in s or '1' in s:
        if '0' in s:
            s = s.replace('0','1',1)
        if ''