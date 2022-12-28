def valor(num):
    if num > 0:
        return 'Positivo'
    else:
        return 'Negativo'
    
        
num = int(input('Digite um valor: '))
valor(num)

print(valor(num))
