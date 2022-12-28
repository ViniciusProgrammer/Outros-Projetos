import math
x = int(input(''))
y = int(input(''))
z = int(input(''))
print('{} + {} + {} = {}'.format(x ** 2, y ** 2, z ** 2, ((x ** 2 + y ** 2 + z ** 2) ** (1/3))))
print('{} + {} = {}' .format(x ** y, y ** z, (x ** y + y ** z)))
print('cos{} + sin {} = {}'.format(x ** 2 + y ** 2, y ** 2 + z ** 2, math.sin(x ** 2 + y ** 2) + math.cos(y ** 2 + z ** 2)))
print('log {} + log {} + log {} = {}'.format(math.log(x), math.log(y), math.log(z), (math.log(x) + math.log(y) + math.log(z)) **(x + y + z)))
