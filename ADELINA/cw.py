n = int(input())
d = '1'
res = 'NO'
for i in range(10**10):
    if int(d) % n == 0:
        res = d
        break
    d += '1'
if res != 'NO':
    print(int(res))
else:
    print(res)