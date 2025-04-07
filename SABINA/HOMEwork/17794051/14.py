s = 343**5 + 343**4 + 49**6 - 7**13 - 21
a = 0
while s > 0:
    a = str(s % 7) + str(a)
    s = s//7
print(len(set(a)))
