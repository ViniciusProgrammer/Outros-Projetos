def valores(num_valores):
    valor = num_valores
    return valor

    
def textos(num_textos):
    texto = num_textos
    return texto
    
    
num_valores = []
num_textos = []

num1 = int(input('Informe a quantidade de valores: '))

for c in range(0, num1):
    num_valores.append(int(input('Digite um número: ')))

num2 = int(input('Informe a quantidade de textos: '))

for i in range(0, num2):
    num_textos.append(input('Digite um texto: '))
            
print('Os numeros digitados foram')

for k in num_valores:
    print(k)
    
print('Os textos digitados foram')

for j in num_textos:
    print(j)
    