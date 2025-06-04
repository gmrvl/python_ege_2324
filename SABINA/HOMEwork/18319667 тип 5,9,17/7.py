cnt = 0
for n in range(10**7,10**9):
    b = bin(n)[2:]
    r = str(b)+str(bin(n%4)[2:])
    r = int(r,2)
    print(r)
    if 10**9 <= r <= 1789456123:
        cnt += 1

print(cnt)
