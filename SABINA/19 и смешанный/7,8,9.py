def f(s,m):
    if s >= 69:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s+1,m-1), f(s+4,m-1),f(s*5,m-1)]
    return any(h) if m % 2 != 0 else all(h) # all(h) меняется на any(h), когда в 19 неудачный первый ход Пети
print([s for s in range(1,69) if f(s,2)]) # если в 19 неудачный ход, то меняешь на ани, а затем снова меняешь на олл для 20 и 21
print([s for s in range(1,69) if not f(s,1) and f(s,3)])
print([s for s in range(1,69) if not f(s,2) and f(s,4)])