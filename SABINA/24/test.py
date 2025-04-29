s = open('test.txt').readline()
s = s.replace('bd','b d')
s = s.split(' ')
print(max(len(ps) for ps in s)) #генератор списков с подстрокой ps, максимальную длину которой мы выводим в ответ