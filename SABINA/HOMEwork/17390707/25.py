for i in range( 35000000,40000001):
    r = []
    t = []
    for d in range(35000000,40000001):
        if i % d == 0:
            r.append(d)
        if len(set(r)) == 5:
            for k in range(len(r)):
                if r[k] % 2 == 1:
                    t.append(r[k])
print(t)

