def f(a,b,m):
    if a+b >= 39:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a,b,m-1),]
    return any(h) if m % 2 != 0 else all(h)
print([s for s in range(1,24) if f(s,2)])
print([s for s in range(1,24) if not f(s,1) and f(s,3)])
print([s for s in range(1,24) if not f(s,2) and f(s,4)])