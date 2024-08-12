count = 0
for i in range(0, 8**5, 2):
    oc = oct(i)[2:] #перевод в восьмеричную систему
    while len(oc) < 5: #восьмибитное число
        oc = '0' + oc
    if oc[0] != '1' and oc.count('2') > 1:
        count += 1
print(count)
