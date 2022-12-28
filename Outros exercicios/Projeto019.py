lista = []
nomes = int(input('Quantos nomes? '))

for c in range(0, nomes):
    lista.append(input('Digite um nome: '))
    
lista.sort(reverse=(True))
print('Você digitou:')

for k in lista:
    print('')
    print(k)
