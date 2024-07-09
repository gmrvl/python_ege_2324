for n in range(1, 1001):
    b_n = bin(n)[2:]
    summ = b_n.count('1')
    if summ % 2 == 0:
        b_n += '00'  # это и строка 7 эквивалентны
    else:
        b_n = b_n + '10'
    r = int(b_n, 2)
    if r > 43:
        print(r)
        break

