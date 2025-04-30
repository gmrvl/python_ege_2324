from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n//10)+n%10
    if n % 2 == 1:
        return f(n//10)
c = 0
for n in range(10**9, 2*(10**9)):
    f(n)
    if f(n) == 0:
        c += 1
print(c)
