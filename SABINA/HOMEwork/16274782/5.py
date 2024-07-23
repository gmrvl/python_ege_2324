a = set()
count = 0
for n in range(10, 1000):
    b = bin(n)[3:]
    s = int(b, 2)
    s = n - s
    a.add(s)
print(len(a))
