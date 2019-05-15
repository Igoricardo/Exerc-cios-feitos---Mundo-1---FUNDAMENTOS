from random import choice
a = input('Informe o 1° aluno:')
b = input('Informe o 2° aluno:')
c = input('Informe o 3° aluno:')
d = input('Informe o 4° aluno:')
s = [a, b, c, d]
print('E o aluno sorteado para apagar o quadro negro foi: {}'.format(choice(s)))

