for n in range(10000):
    s = bin(n)[2:]
    s = s.replace('0','*')
    s = s.replace('1','0')
    s = s.replace('*','1')
    s = int(s, 2)
    s = n - s
    if s == 999:
        print(n)
        break
