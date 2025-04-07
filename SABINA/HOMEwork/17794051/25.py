for i in range(700001,1000000):
    d = []
    for l in range(2,int(i**0.5) + 1):
        if i % l == 0:
            d.append(l)
            d.append(i// l)
    if len(d) == 0:
        d.append(0)
    d = set(d)
    m = max(d) + min(d)
    if m % 10 == 4:
        print(i,m)