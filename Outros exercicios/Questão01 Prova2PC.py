D = int(input('Dist: '))
M = int(input('Media: '))

Cont = 0
num_voltas = 0
while Cont <= D:
    Cont += M
    num_voltas += 1
print(num_voltas)
