def f(x,y,a):
    return ((2*x + 3*y) != 60) or (a >= x) or (a >= y)
print(min(a for a in range(0,200) if all( f(x,y,a) == 1 for x in range(0,2000) for y in range(0,2000))))