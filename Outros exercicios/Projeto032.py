valor = int(input('Informe o valor: '))

cem = int(valor/ 100)
valor = valor - (cem*100)

cinquenta = int(valor/50)
valor = valor - (cinquenta*50)

vinte = int(valor/20)
valor = valor -(vinte*20)

dez = int(valor/10)
valor = valor - (dez*10)

cinco = int(valor/5)
valor = valor - (cinco*5)

dois = int(valor/2)
valor = valor - (dois*2)

um = valor

print(cem, 'Notas de 100,00')
print(cinquenta, 'Notas de 50,00')
print(vinte, 'Nots de 20,00')
print(dez, 'Notas de 10,00')
print(cinco, 'Notas de 5,00')
print(dois, 'Notas de 2,00')
print(um, 'Notas de 1,00')
