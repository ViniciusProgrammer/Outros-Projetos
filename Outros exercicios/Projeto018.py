n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

primos = 0

if n2 > n1:
    for c in range(n1, n2+1):
        cont = 0
        for i in range(1, c + 1):
            if c % i == 0:
                cont += 1
        if cont == 2:
            primos += 1
print(primos)
    