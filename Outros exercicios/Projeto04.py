num_A = int(input('Digite o valor de A: '))
num_B = int(input('Digite o valor de B: '))
if num_A > num_B:
    for c in range(num_A, num_B - 1, -1):
        print(f'{c}', end=' ')
elif num_A < num_B:
    for i in range(num_A, num_B + 1):
        print(f'{i}', end=' ')
