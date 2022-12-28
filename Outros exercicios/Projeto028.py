def soma(lista):
    tot_soma = 0
    for k in range(0, len(lista)):
        tot_soma += lista[k]
    print(tot_soma)
    
    
lista = []

num = int(input('Informe a quantidade de valores você quer adicionar na lista: '))

for c in range(0, num):
    lista.append(int(input('Digite um valor: ')))
    
soma(lista)
