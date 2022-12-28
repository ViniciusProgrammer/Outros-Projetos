soma = 0
media = 0
for c in range(1, 6):
    valor = int(input(f'Informe o {c}° valor: '))
    soma += valor
    media = soma/c
print('A soma vale {}'.format(soma))
print('A media vale {}'.format(media))
