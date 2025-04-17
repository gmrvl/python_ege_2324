def f(a,x,y):
    return ((x <= 9) <= (x*x <= a)) and ((y*y <= a) <= (y <= 9))

print(min(a for a in range(0,200) if all(f(a,x,y) == 1 for x in range(0,2000) for y in range(0,2000))))