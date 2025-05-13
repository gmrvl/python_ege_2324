f = ['ABCDACEB']
maxx = 0
for i in f:
    if i.count('A') < 25:
        for j in i:
            maxx = max(i.rfind(j) - i.find(j), maxx)
print(maxx)