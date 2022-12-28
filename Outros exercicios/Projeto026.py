#Exercicio 17 só que agora utilizando funções
def linhas(num):
    for c in range(1, num + 1):
        for i in range(1, c + 1):
            print(f'{c}', end=' ')
        print('')
        
    
num = int(input('Digite um numero: '))

linhas(num)
