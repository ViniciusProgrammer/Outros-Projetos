from math import ceil
windows = []
cont_windows = 0
unix = []
cont_unix = 0
linux = []
cont_linux = 0
netware = []
cont_net = 0
mac_os = []
cont_mac = 0
outro = []
cont_outro = 0

while True:
    dados = int(input(('Informe o sistema operacional que você prefere: ')))
    if dados == 1:
        windows.append(dados)
        cont_windows += 1
    elif dados == 2:
        unix.append(dados)
        cont_unix += 1
    elif dados == 3:
        linux.append(dados)
        cont_linux += 1
    elif dados == 4:
        netware.append(dados)
        cont_net += 1
    elif dados == 5:
        cont_mac += 1
    elif dados == 6:
        outro.append(dados)
        cont_outro += 1
    else:
        if dados == 0:
            print('Finalizando a contagem...')
            break
print('Sistema Operacional =-=-=-=-=-=- Votos =-=-=-=-=-=-=-=  % =-=-=-')
print(f'Windows                          {cont_windows}                        {cont_windows/100}%')
print(f'Unix                             {cont_unix}                        {cont_unix/100}%')
print(f'Linux                            {cont_linux}                        {cont_linux/100}%')
print(f'Netware                          {cont_net}                        {cont_net/100}%')
print(f'Mac_OS                           {cont_mac}                        {cont_mac/100}%')
print(f'Outros                           {cont_outro}                        {cont_outro/100}%')
print(f'O total                          {cont_windows + cont_unix + cont_linux + cont_net + cont_mac + cont_outro}')
