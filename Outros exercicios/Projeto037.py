num_valores = int(input('Quantos valores deseja adicionar? '))

lista_valores = []
soma_media = 0
acima_media = 0

for c in range(0, num_valores):
    num = float(input('Informe um valor: '))
    lista_valores.append(num)

for k in lista_valores:
    soma_media += k
    
for k in lista_valores:
    if k > soma_media/len(lista_valores):
        acima_media +=1
        
print(f'Foram lidos {len(lista_valores)} valores')
print(lista_valores)
print(lista_valores[::-1])
print('Media dos valores: {:.2f}'.format(soma_media/len(lista_valores)))
print(f'{acima_media} valores acima de {soma_media/len(lista_valores):.2f}')
