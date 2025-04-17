def f(x,y,a):
    return ((y<20) <= (x>70)) or ((not(x<a)) <= (y > a))
print(list(a for a in range(0,200) if all(f(x,y,a) == 1 for x in range(0,2000) for y in range(0,2000))))
