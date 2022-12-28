valor = int(input('Informe o valor: '))

lista_valores = []

for c in range(0, valor):
    lista_valores.append(int(input('Digite um valor: ')))
    
op = int(input('Digite a Operação: 0 ou 1: '))
a = int(input('Digite o A: '))
b = int(input('Digite o B: '))

if op == 0:
    total = lista_valores[a-1] + lista_valores[b-1]
    print('{} + {} = {}'.format(lista_valores[a - 1], lista_valores[b - 1], total))
    
else:
    total = lista_valores[a - 1] * lista_valores[b - 1]
    print('{} * {} = {}'.format(lista_valores[a -1], lista_valores[b-1], total))
    