cnt = 0
f = open('09 (2).csv')
for i in f:
    summ1 = 0  # - сумма повторяющихся,
    delit1 = 0  # - их кол-во
    summ2 = 0  # - сумма не повторяющихся,
    delit2 = 0  # - их кол-во
    sr1, sr2 = 0, 0
    a = list(map(int, i.split(';')))
    if len(set(a)) != len(a):
        for k in range(len(a)):
            if a.count(a[k]) > 1:
                summ1 += a[k]
                delit1 += 1
            else:
                summ2 += a[k]
                delit2 += 1
            if delit1 > 0:
                sr1 = summ1 / delit1
            if delit2 > 0:
                sr2 = summ2 / delit2
    if sr2 > sr1:
        cnt += 1
print(cnt)
