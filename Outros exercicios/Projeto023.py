def mediaAritmetica(notas):
    media = ((notas[0]) + (notas[1]) + (notas[2]))/3    
    return media


def mediaPonderada(notas):
    media = ((notas[0] * 5) + (notas[1] * 3) + (notas[2] * 2))/10
    return media

    
notas = []

for c in range(0, 3):
    notas.append(float(input('Informe uma nota: ')))
    
letra = input('Qual a media você deseja ver? ')

if letra.upper() == 'A':
    print('A média é {}'.format(mediaAritmetica(notas)))
    
elif letra.upper() == 'P':
    print('A media é {}'.format(mediaPonderada(notas)))
    