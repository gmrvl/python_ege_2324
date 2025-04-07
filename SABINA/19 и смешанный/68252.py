from math import sqrt


def poisk_del(s):
    d = []
    stop = int(sqrt(s))
    for j in range(1, stop + 1):
        if s % j == 0:
            d.append(j)
            if s // j != j:
                d.append(s // j)
    d.remove(s)
    return d


count = 0
res = []
for s in range(2, 46):
    d = poisk_del(s)
    true = 0
    for petya in d:
        if s + petya <= 45:
            d_v = poisk_del(s + petya)
            for vanya in d_v:
                if s + petya + vanya > 45:
                    true += 1
                    break

    if true == len(d):
        count += 1
        res.append(s)

print(count, res)
