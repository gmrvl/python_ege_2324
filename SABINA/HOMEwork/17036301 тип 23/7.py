def f(x,y):
    if x == y:
        return 1
    if x > y or x==15:
        return 0
    if x < y :
        return f(x+1,y) + f(x+3,y) + f(x*3,y)
print(f(7,14)*f(14,20))