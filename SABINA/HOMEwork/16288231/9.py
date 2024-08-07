count = 0
for i in range(1, 9876543211):
    s = str(i)
    a = set(s)
    if (len(a) == len(s)) and (i % 5 == 0):
        count += 1
print(count)
