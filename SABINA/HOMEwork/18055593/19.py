from functools import lru_cache

@lru_cache()
def f(n):
    if n == 1: return 1
    if (n > 1) and (n % 2 == 1): return n + f(n-2)
    if n % 2 == 0: return n * f(n-1)

for n in range(1,61): f(n)
print(f(60))