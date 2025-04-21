for i in range(800001, 1000000):
    dells = []
    for l in range(2, int(i**0.5) + 1):
        if i % l == 0:
            dells.append(l)
            dells.append(i // l)
    if len(dells) == 0:
        dells.append(0)
    dells = set(dells)
    m = max(dells)+min(dells)
    if m % 10 == 4:
        print(i, m)
