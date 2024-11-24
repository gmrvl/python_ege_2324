# F(0)=0;
#
# F(n)=F(n / 2), если n > 0 и при этом чётно;
#
# F(n)=1+F(n − 1), если n нечётно.

def F(n):
    if n == 0:
        return 0
    elif n % 2 == 0:     # можно не писать n>0, так как, если будет 0, то попадет в первый if
        return F(n / 2)
    else:
        return 1 + F(n - 1)

count = 0
for n in range(1, 1001):
    if F(n) == 3:
        count += 1
print(count)