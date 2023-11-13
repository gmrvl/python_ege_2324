for n in range(1, 101):
    b_n = bin(n)[2:]
    res = ''
    # b_n = int(b_n)
    # while b_n != 0:
    #     res += str(b_n % 10)
    #     b_n //= 10
    for i in b_n:
        res = i + res
    while res[0] == '0':
        res = res[1:]
    res10 = int(res, 2)
    if res10 == 13:
        print(n)
