s = (343**5)-(7**9)+48
r = ''
while s != 0:
    r = str(s % 7) + r
    s //= 7
print(r.count('6'))
