pares = []
impares = []
valores = []

for c in range(0, 10):
    num = int(input('Informe um valor: '))
    valores.append(num)
    
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)
        
print('A lista de pares = {} e a lista de impares é {}'.format(pares, impares))
print(valores)
