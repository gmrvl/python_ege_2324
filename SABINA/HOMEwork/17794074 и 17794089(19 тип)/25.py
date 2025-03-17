for i in range(800001,1000000):
    for l in range(2,(i**0.5) + 1):
        m = max(l)+min(l)
        if i % m == 0:
            if m % 10 == 4:
                print(i,m)
