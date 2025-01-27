count = 0
for x in range(0, 16): # это 10000 в двоичной - 1 == 1111 в двоичной = 15 в десятичной
    for y in range(0, 256):
        for z in range(0, 256):
            a = bin(x)[2:] + bin(y)[2:] + bin(z)[2:]
            if a.count('1') % 5 != 0:
                count += 1
print(count)
