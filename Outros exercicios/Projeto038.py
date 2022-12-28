valores = []
quadrado = []
soma_indices = 0

for c in range(0, 10):
    valores.append(int(input('Digite um valor: ')))

print(f'Os valores informados na lista foram {valores}')  
  
for item in valores:
    quadrado.append(item**2)
    soma_indices += item**2
print(f'A soma de todos os índices ao quadrado deram {soma_indices}')
