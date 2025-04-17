from functools import lru_cache

@lru_cache()
def f(n):
    if n == 1: return 1
    if n > 1: return f(n-1)+n


for n in range(1,40): f(n)
print(f(40))