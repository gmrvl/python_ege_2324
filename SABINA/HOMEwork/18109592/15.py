def f(x,y,a):
    return (x > a) or (y > x) or (2*y + x < 110)
print(max(a for a in range(0,200) if all(f(x,y,a) == 1 for x in range(0,1000) for y in range(0,1000))))