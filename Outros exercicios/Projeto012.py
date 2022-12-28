bolsa = 400
valor_por_mes = float(input('Quanto você irá reservar? '))
meses = int(input('Quantidade de meses? '))
print('O total que vc irá ter após {} meses é {:.0f}'.format(meses, (valor_por_mes * (bolsa/100)) * meses))
