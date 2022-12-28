altura = []
idade = []

for c in range(0, 5):
    altura.append(float(input('Informe a sua altura: ')))
    idade.append(int(input('Informe a sua idade: ')))

idade.sort(reverse=True)
altura.sort(reverse=True)

print(idade)
print(altura)
