for i in range(2, 1000):
    b = bin(i)[2:]
    b = b[:-1] + b[1]*2
    r = int(b, 2)
    if r > 92:
        print(i)
        break

    