a = int(input())
b = int(input())
c = int(input())
d = int(input())

res1 = a + c
res2 = b + d
print(res1, res2)
dells1 = []
dells2 = []
de = 2
while de*de <= res1:
    while res1 % de == 0:
        dells1.append(de)
        res1 = res1 // de
    de += 1
if res1 > 1:
    dells1.append(res1)
print(dells1)
de = 2
while de*de < res2:
    while res2 % de == 0:
        dells2.append(de)
        res2 = res2 // de
    de += 1
if res2 > 1:
    dells2.append(res2)
print(dells2)

for i in dells1:
    if i in dells2:
        dells1.remove(i)
        dells2.remove(i)
print(dells1, dells2)
