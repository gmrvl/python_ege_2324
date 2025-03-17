def win1(s):
    return (s+1) >= 31 or (s*3 - 2)>= 31
def los1(s):
    return not(win1(s)) and win1(s+1) and win1(s*3 - 2)
for s in range(1,31):
    if los1(s):
        print(s)
