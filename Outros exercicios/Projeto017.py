num = int(input('Digite o valor: '))

if num > 0 and num < 10:
    for c in range(1, num + 1):
        for i in range(1, c + 1):
            print(c, end=' ')
        print('')
            