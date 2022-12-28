texto1 = input('Primeiro texto: ')
texto2 = input('Segundo texto: ')
texto3 = input('Terceiro texto: ')

print('Seguem os textos na ordem!')

if texto1 < texto2 < texto3:
    print('1° {}\n2° {}\n3° {}'.format(texto1, texto2, texto3))
elif texto2 < texto1 < texto3:
    print('1° {}\n2° {}\n3° {}'.format(texto2, texto1, texto3))
elif texto2 < texto3 < texto1:
    print('1° {}\n2° {}\n3° {}'.format(texto2, texto3, texto1))
elif texto1 < texto3 < texto2:
    print('1° {}\n2° {}\n3° {}'.format(texto1, texto3, texto2))
elif texto3 < texto1 < texto2:
    print('1° {}\n2° {}\n3° {}'.format(texto3, texto1, texto2))
elif texto3 < texto2 < texto1:
    print('1° {}\n2° {}\n3° {}'.format(texto3, texto2, texto1))
    