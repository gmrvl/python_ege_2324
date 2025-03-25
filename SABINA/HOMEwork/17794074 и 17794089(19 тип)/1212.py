def prostoe(n):
    k = 2
    while k ** 2 <= n:
        if n % k == 0: return False
        k += 1
    return True


def algo(s):
    while not '00' in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('012', '30', 1)
        s = s.replace('010', '00', 1)
    print(s)
    return sum(map(int, s))


for n in range(49, 100):
    s = '0' + '2' * n + '1' * 48 + '0'
    if prostoe(algo(s)):
        print(n)
        break