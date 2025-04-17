def f(x,a):
    return (x & 29 != 0) <= ((x & 12 == 0) <= (x & a != 0))
print(min(a for a in range(0,200) if all(f(x,a) == 1 for x in range(1,2000))))