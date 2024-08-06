for n in range(101, 100000):
    s = str(n)
    a = []
    for i in range(len(s)-2):
        t = int(s[i:i+3])
        a.append(t)
    if (max(a) - min(a)) == 415:
        print(n)
        break


