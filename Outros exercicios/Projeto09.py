pares = impares = 0
for c in range(1, 11):
    valor = int(input('Informe o {}° valor: '.format(c)))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Ao todos foram encontrados {pares} números pares e {impares} impares.')
