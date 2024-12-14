def f(x,y):
    if x == y:
        return 1
    if x > y or x == 12:
        return 0
    if x < y:
        return f(x+1,y) + f(x*2,y)
print(f(2,11)*f(11,24))

def f(a,b):
    if a == b:
        return 1
    if a > b or a == 11:
        return 0
    if a < b:
        return f(a+1,b) + f(a*2,b)
print(f(2,12)*f(12,24))