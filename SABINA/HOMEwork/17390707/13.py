cnt = 0
for x in range(0,16):
    for y in range(0,256):
        for z in range(0,256):
            f = bin(x)[2:] + bin(y)[2:] + bin(z)[2:]
            if f.count('1') % 5 != 0:
                cnt += 1
print(cnt)