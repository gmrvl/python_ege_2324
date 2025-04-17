from functools import lru_cache

@lru_cache()
def f(n):
    if n == 1: return 1
    if n > 1: return f(n-1) * n


for n in range(1,2024): f(n)
print((f(2024)-f(2023))/f(2022))