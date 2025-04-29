f = open('inf_26_04_21_24.txt').readlines()
for i in f:
    k = 0
    p = []
    r = ''
    if i.count('A') < 25:
        for n in i:
            r = r + n
            if len(r) == len(set(r)):
                k += 1
            else:
                k += 0
                p.append(k)
                i.split(n)
