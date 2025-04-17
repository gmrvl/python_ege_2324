from functools import lru_cache

@lru_cache()
def f(n):
    if n <= 2: return n + 3
    if n > 2: return f(n-1)+ f(n-2)


for n in range(1,8): f(n)
print(f(7))