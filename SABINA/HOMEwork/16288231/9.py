count = 0
for i in range(100000000, 1000000000):
    i = str(i)
    f = True
    a = set(i)
    if len(a) != len(i):
        f = False
    if f and (int(i) % 5 == 0):
        count += 1
print(count)