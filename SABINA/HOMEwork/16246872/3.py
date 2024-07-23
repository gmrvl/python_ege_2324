count = 0
for i in range(9876543210, -1, -5):
    s = str(i)
    a = set(s)
    if len(s) == len(a):
        count += 1
print(count)
