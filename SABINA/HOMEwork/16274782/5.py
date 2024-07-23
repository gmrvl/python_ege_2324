count = 0
for n in range(10, 1000):
    b = bin(n)[3:]
    while b[0] == '0' and len(b) > 1:
        b = b[1:]
    s = int(b, 2)
    s = int(b) - n
    if s:
        count +=1
print(count)