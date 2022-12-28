def valores(num_valores):
    valor = (f'{num_valores}')
    return valor


def textos(num_textos):
    textos =(f'{num_textos}')
    return textos

        
num_valores = []
num_textos = []
    
num1 = int(input('Informe a quantidade de numeros a serem incluidos na lista: '))
for c in range(0, num1):
    num_valores.append(int(input('Digite um valor: ')))

num2 = int(input('Informe a quantidade de textos a serem adicionados: '))
for i in range(0, num2):
    num_textos.append(input('Informe o texto: '))
    
print('Os valores adicionados foram: ')

for k in num_valores:
    print(k)
    
print('Os textos adicionados foram: ')

for t in num_textos:
    print(t)
