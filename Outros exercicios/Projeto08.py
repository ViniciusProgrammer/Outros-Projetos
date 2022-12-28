maior = 0
for c in range(1, 6):
    valor = int(input('Informe o {}° valor: '.format(c)))
    if valor == maior:
        maior = valor
    else:
        if valor > maior:
            maior = valor
print(f'O maior valor digitado foi {maior}')
