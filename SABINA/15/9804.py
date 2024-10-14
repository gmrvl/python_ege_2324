# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)
res = 0
for a in range(0, 1000):
    ok = 1
    for x in range(0, 1000):
        if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))) == 0:
            ok = 0
    if ok:
        res = a
        break
print(res)
