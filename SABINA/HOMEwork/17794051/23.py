def f(x,y):
    if x == y:
        return 1
    if x < y:
        return f(x+3,y)+f(x+4,y)+f(x+5,y)
    if x > y:
        return 0
print(f(22,42))