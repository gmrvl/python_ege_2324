cnt = 0
for n in range(10000000):
    r = bin(n)[2:]
    r += bin(n % 4)[2:]
    r = int(r,2)
    #print(r)
    if r > 1100000000 and r < 1987653210:
        cnt+=1
print(cnt)
