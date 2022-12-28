#Maior e Menor valor
num_1 = int(input('Digite o primeiro valor: '))
num_2 = int(input('Digite o segundo valor: '))
maior = 0
menor = 0
if num_1 > num_2:
    maior = num_1
    menor = num_2
    print('{} é o maior e {} é menor'.format(maior, menor))
elif num_2 > num_1:
    maior = num_2
    menor = num_1
    print('{} é o maior {} é o menor'.format(maior, menor))
