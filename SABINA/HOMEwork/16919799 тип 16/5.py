def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return F(n-1) + 2**(n-1)
    else:
        return 2*F(n-2)
print(F(26))