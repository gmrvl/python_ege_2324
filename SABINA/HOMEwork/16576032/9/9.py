cnt = 0
f = open('09 (2).csv')
summ1 = 0   #  - сумма повторяющихся,
delit1 = 0   # - их кол-во
for i in f:
     a = list(map(int, i.split(';')))
     if len(set(a)) != len(a):
         for k in range(len(a)):
             if a[k] > 1:
                 summ1 += a[k]
                 delit1 += 1
             sr1 = summ1/ delit1
             sr2 = sum(set(a))/ len(set(a))
     if sr2 > sr1:
         cnt+=1
print(cnt)
