a = '123'
print(sum(map(int,a)))
print(a[2:])
p = ''
n = 123
while n > 0:
    p = str(n % 3) + str(p)
    n = n // 3
print(p)

print(bin(5)[2:])