def F(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return F(n/2)
    else:
        return 1 + F(n-1)

cnt = 0
for n in range(1, 500):
    if F(n) == 3:
        cnt += 1
print(cnt)