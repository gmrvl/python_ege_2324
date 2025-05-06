for n in range(2000000,3000001):
    for delit in range(1,int(str(n**0,5))+1):
        r = []
        if n % delit == 0:
            if delit <= (n // delit):
                r.append((n // delit)-delit)
            else:
                r.append(delit-(n // delit))
        if len(r) >= 3 and max(r) <= 115:
            print(n)