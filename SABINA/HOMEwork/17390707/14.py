s = 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82
a = 0
while s > 0:
    a = str(s % 16) + str(a)
    s = s // 16
a = str(a)
print(len(set(a)))