from random import shuffle
a = input('Informe o 1° grupo:')
b = input('Informe o 2° grupo:')
c = input('Informe o 3° grupo:')
d = input('Informe o 4° grupo:')
g = [a, b, c, d]
shuffle(g)
print('A ordem dos grupos a apresentar os trabalhos é: {}'.format(g))
