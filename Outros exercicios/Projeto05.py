c = 1
cont = 0
while c < 11:
    valor = int(input(f'Informe o {c}° valor: '))
    c += 1
    if valor > 30:
        cont += 1
print(f'Foram encontrados {cont} maiores que 30')
