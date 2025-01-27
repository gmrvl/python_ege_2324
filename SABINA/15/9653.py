p=[int(i) for i in range(10,30)]
q=[int(i) for i in range(13,19)]
a=[int(i) for i in range(10,30)]
for x in range(1,100):
    if not(((x in a)<=(x in p)) or(x in q)):
        a.remove(x)
print(len(a)-1)