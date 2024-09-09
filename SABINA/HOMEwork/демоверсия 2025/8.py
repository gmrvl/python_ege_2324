count = 0
for i in range(12**4,12**5):
    a = ''
    while i > 0:
        a = str(i % 12) + a
        i = i // 12
    n = '91011'
    if a.count('7') == 1 and a.count(''):

