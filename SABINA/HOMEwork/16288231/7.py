count = 0

for i in range(1000, 10000):
    s = str(i)
    a = set(s)
    if len(a) == len(s):
        if (int(s[0]) % 2 + int(s[1]) % 2 == 1) and (int(s[1]) % 2 + int(s[2]) % 2 == 1) and (int(s[2]) % 2 + int(s[3]) % 2 == 1):
            count += 1
print(count)

