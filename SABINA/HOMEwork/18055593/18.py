from functools import lru_cache

@lru_cache()
def f(n):
    if n < 10: return n
    if n >= 10: return f(n)
for n in range(1,11): f(n)
print(f(10))