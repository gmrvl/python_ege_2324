for n in range(1,101):
    i = bin(n)[2:]
    r = i[::-1] #переворачивает
    r = r.lstrip('0') #удаляет ведущие нули
#    print(r)
    r = int(r,2)
#    print(r)
    if r == 11:
        print(n)

