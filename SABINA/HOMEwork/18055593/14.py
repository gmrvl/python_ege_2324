def f(x,a):
    return (x & 49 == 0) <= ((x & 28 != 0) <= (x & a != 0))

print(min(a for a in range(0,200) if all( f(x,a) == 1 for x in range(0,2000))))