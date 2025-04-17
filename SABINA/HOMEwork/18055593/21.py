from functools import lru_cache

@lru_cache()
def f(n):
    if n >= 2025: return n
    if n < 2025: return n + 3 + f(n+3)


for n in range(1,20): f(n)
print(f(23) - f(21))