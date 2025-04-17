from functools import lru_cache

@lru_cache()
def f(n):
    if n == 1: return 1
    if n == 2: return 1
    if n > 2: return f(n-2) * n


for n in range(1,7): f(n)
print(f(7))