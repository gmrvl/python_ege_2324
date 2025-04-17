from functools import lru_cache

@lru_cache()
def f(n):
    if n == 1: return 1
    if n == 2: return 1
    if (n > 2) and (n%2==0): return (4*n - f(n-3))/8
    if (n > 2) and (n%2==1): return (4*n - f(n-1) + f(n-2))/8


for n in range(1,52): f(n)
print(f(52)-f(38))