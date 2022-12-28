medias_alunos = []
alunos_acima_media = 0

for aluno in range(3):
    soma_media = 0
    print(f'Calculando a média do {aluno + 1}° aluno(a) ')
    for nota in range(4):
        soma_media += float(input(f'Digite a {nota + 1} nota do {aluno + 1} aluno(a): '))
    medias_alunos.append(soma_media/4)
    
    if medias_alunos[aluno] >= 7.0:
        alunos_acima_media +=1

        
print(medias_alunos)
print(alunos_acima_media)
