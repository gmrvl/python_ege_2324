# zxyx7+xy836=wzx64
for p in range(9, 11):
    for x in range(1, p):
        for y in range(0, p):
            for z in range(1, p):
                for w in range(1, p):
                    a1 = z*(p**4) + x*(p**3) + y*(p**2) + x*p + 7
                    a2 = x * (p ** 4) + y * (p ** 3) + 8 * (p ** 2) + 3 * p + 6
                    a3 = w * (p ** 4) + z * (p ** 3) + x * (p ** 2) + 6 * p + 4
                    if a1 + a2 == a3:
                        print(x*(p**3) + y*(p**2) + z*p + w)
