from random import choice
from time import sleep
n = int(input('Informe um número de 0 a 5:'))
s = [0, 1, 2, 3, 4, 5]
x = choice(s)
print('Loading...')
sleep(2)
if n == x:
    print('Parabéns, você acertou!, eu pensei em {} e você disse justamente o número {}.'.format(x, n))
else:
    print('Você errou! pensei em {} e você me informou o número {}.'.format(x, n))

# from random randint
# c = randint(0, 5)
# Esta é outra forma de utilizar até mais facil, de fazer o computador ou o programa escolher um número aleatório.
# No exemplo em questão, de 0 a 5.