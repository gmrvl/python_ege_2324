# две функции (сложный номер)

from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 3210: return 1
    if n < 3210: return f(n+3) + 7

@lru_cache(None)
def g(n):
    if n < 10: return n
    if n >= 10: return g(n-3)+5
#форы для двух функций
for n in range(10,3000): g(n)  # диапозон фора смотрится примерно от ограничения до того, что вызывается в принте
for n in range(3210,15,-1): f(n) # снова от ограничения до того, что в принте ( только из-за того, что в другом порядке нужно сделать шаг -1)

print(f(15) - g(3000))