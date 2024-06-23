a = 2 * 216**8 + 4*36**12 + 6**15 - 1296
s = ''
while a>0:
    s = str(a % 3) + s
    a = a // 3
print(s.count('2'))
