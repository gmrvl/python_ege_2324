from functools import lru_cache
def f(a,b):
    if b == 0: return a
    if a >= b >= 0: return f(a-b,b)
    if a <b: return f(b,a)
for b in range(1,10):
    for a in range(1, 10):
        print(a,b,f(a,b))

