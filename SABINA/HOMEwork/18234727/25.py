for n in range(2000000,3000001):
    sqr = int(n ** 0.5)
    r = []
    for delit in range(1, sqr + 1):
        if n % delit == 0:
            if delit <= (n // delit) and (n // delit) - delit <= 115:
                r.append((n // delit)-delit)
            else:
                if (n // delit) - delit <= 115:
                    r.append(delit - (n // delit))
        if len(r) >= 3:
            print(n)