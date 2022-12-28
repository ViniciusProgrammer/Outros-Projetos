valores = []
soma = 0
produto = 1

for c in range(5):
    num = int(input('Informe um valor: '))
    valores.append(num)
    
for k in valores:
    soma += k
    produto *= k    
print(soma)
print(produto)
print(f'A lista possui os seguintes valores: {valores}')
