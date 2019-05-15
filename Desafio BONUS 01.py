#Exercício / teste sobre o terminal de cores em PYTHON
print('* TESTE *'*14)
print('\033[1;33m # \033[m' *26)
print('\n Olá mundo!')
print('\033[1;31;40m Olá mundo!') 
print('\033[1;32;41m Olá mundo!')
print('\033[1;33;42m Olá mundo!')
print('\033[1;34;43m Olá mundo!')
print('\033[1;35;44m Olá mundo!')
print('\033[1;36;45m Olá mundo!')
print('\033[1;37;46m Olá mundo!')
print('\033[1;40m Olá mundo!')
print('\033[1;41m Olá mundo!')
print('\033[1;42m Olá mundo!')
print('\033[1;43m Olá mundo!')
print('\033[1;44m Olá mundo!')
print('\033[1;45m Olá mundo!')
print('\033[1;46m Olá mundo!')
print('\033[1;47m Olá mundo!\033[m')
print('\033[1;31m -=- \033[m'*26)

#Atribuindo cor utilizando nas chaves que chamam as variáveis no .format
a = 10
b = 25
print('O primeiro valor é \033[4;46m {}\033[m e o segundo valor é \033[4;42m {}\033[m'.format(a, b))

#Atribuindo cor dentro do .format
nome = 'IGOR'
print('Olá {}{}{}!'.format('\033[1;4;41m', nome, '\033[m'))

#Criando uma variável / dicionário de cores
c = {'azul':'\033[1;34m',
    'amarelo':'\033[1;33m',
    'vermelho':'\033[1;21m',
    'limpa':'\033[m'}
    
n = str(input('Informe um nome:')).strip().upper()
print('Olá tudo bem? NÃO?! então foda-se {}{}{}'.format(c['azul'], n, c['limpa']))









