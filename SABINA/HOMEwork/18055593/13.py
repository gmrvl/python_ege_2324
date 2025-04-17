def f(y,x,a):
    return ((x < a) <= ((x**2) < 100)) and (((y**2) <= 64) <= (y <= a))

print(len(list(a for a in range(0,200) if all(f(y,x,a) == 1 for x in range(0,2000) for y in range(0,2000)))))