def linhas(num):
    for c in range(1, num + 1):
        for i in range(1, c + 1):
            print(f'{i}', end= ' ')
        print('')

    
num = int(input('Digite um número: '))

linhas(num)
