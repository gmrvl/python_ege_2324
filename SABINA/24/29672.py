f = open('inf_22_10_20_24.txt')
c = 0
for i in f:
    if i.count('E') > i.count('A'):
        c += 1
print(c)
