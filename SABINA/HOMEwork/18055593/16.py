from functools import lru_cache


@lru_cache
def f(n):
    if n == 1: return 5
    if n == 2: return 5
    if n > 2:
        return 5* f(n-1) - 4* f(n-2)

for n in range(1,14): f(n)
print(f(13))