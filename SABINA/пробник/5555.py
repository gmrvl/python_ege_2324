i = 53
n = ''
while i != 0:
    n = str(i%4) + n
    i //= 4
print(n)
print(int('113',4))