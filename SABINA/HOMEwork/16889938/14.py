f = 4**34 + 5*4**22 + 2*4**9 + 82
s = ''
while f > 0:
    s = str(f % 16) + s
    f = f // 3
print(len(set(s)))

