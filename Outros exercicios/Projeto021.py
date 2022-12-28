lista_num = []

for c in range(0, 5):
    lista_num.append(int(input('Digite um valor: ')))

for k in lista_num:
    if k % 2 == 0:
        print(f'O número {k} é PAR!')
    else:
        print(f'O número {k} é IMPAR!')
    