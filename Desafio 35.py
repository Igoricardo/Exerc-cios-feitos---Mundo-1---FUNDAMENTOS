a = float(input('Informe o 1° número:'))
b = float(input('Informe o 2° número:'))
c = float(input('Informe o 3° número:'))
if (b-c) < a < b + c and (a-c) < b < a + c and (a-b) < c < a + b:
    print('VERDADEIRO, é possível formar um triângulo!')
else:
    print('FALSO, não é possível formar um triângulo!')
 