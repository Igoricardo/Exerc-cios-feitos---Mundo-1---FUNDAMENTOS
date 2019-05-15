n = int(input('Informe um número de 0 até 9999:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade:{}\nDezena:{}\nCentena:{}\nMilhar:{}'.format(u, d, c, m))

print('2° forma de fazer o desafio:\n')

n = str(int(input('Informe um número de 0 a 9999:'))+10000)
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(n[4], n[3], n[2], n[1]))
