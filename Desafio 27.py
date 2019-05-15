nome = str(input('Digite seu nome completo:')).strip().upper()
x = nome.split()
print('> O primeiro nome é: {} \n> E o último é: {}'.format(x[0], x[0-1]))
