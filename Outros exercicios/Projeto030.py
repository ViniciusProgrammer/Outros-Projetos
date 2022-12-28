lista = []

for c in range(1, 4):
    lista.append(float(input('Informe uma nota: ')))

media = 0
for k in range(0, len(lista)):
    media += lista[k]


print(f'As notas do aluno são: {lista}')  
  
if len(lista) == 0:
    print('Não foram inserida as notas do aluno!')
else:
    print(f'A média foi {media/len(lista):.1f}')
