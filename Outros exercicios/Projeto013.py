a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
if a > b and a < c:
    print('O valor {} lido em A é o intermediário'.format(a))
elif b > a and b < c:
    print('O valor {} lido em B é o intermediário'.format(b))
elif c > a and c < b:
    print('O valor {} lido em C é o intermediário'.format(c))
elif a > c and a < b:
    print('O valor {} lido em A é o intermediário'.format(a))
elif c > b and c < a:
    print('O valor {} lido em C é o intermediário'.format(c))
elif b > c and b < a:
    print('O valor {} lido em B é o intermediário'.format(b))
else:
    print('Não existe valores intermediários!')
    