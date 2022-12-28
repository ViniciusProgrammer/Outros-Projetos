from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} a {f} de {p} em {p}')
    sleep(2.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(1)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(1)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez')
inicio = int(input('Informe o inicio: '))
fim = int(input('Informe o final: '))
passo = int(input('Informe o passo: '))
contador(inicio, fim, passo)
