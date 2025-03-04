f = open('24_59848.txt').read()
alph = '0123456789ABCDEFGHIJKLMN'
count = 0
max_c = 0
for i in f:
    if i in alph:
        count += 1
    else:
        max_c = max(max_c, count)
        count = 0
max_c = max(max_c, count)
print(max_c)
