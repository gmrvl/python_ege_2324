for n in range(2,1000):
    s = bin(n)[2:]
    if s.count('1') == s.count('0'):
        s = str(s) + str(s[-1])
    else:
        if s.count('1') > s.count('0'):
            s = str(s) + '0'
        else:
            s = str(s) + '1'
    if s.count('1') == s.count('0'):
        s = str(s) + str(s[-1])
    else:
        if s.count('1') > s.count('0'):
            s = str(s) + '0'
        else:
            s = str(s) + '1'
    if s.count('1') == s.count('0'):
        s = str(s) + str(s[-1])
    else:
        if s.count('1') > s.count('0'):
            s = str(s) + '0'
        else:
            s = str(s) + '1'

    s = int(s,2)
    if n > 104 and s % 4 == 0:
        print(n, s)

