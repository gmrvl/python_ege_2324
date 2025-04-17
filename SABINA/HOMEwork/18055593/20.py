from functools import lru_cache

@lru_cache()
def f(n):
    if n == 1: return 1
    if n>1: return f(n-1)*(n+1)


for n in range(1,5): f(n)
print(f(4))