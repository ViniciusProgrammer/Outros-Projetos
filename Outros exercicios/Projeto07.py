cont = 0
soma = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            cont = + 1
            soma += c
            print(c)
print('A soma entre os valores vale {}'.format(soma))
