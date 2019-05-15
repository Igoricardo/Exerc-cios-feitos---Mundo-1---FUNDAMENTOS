import math
ca = float(input('Informe o valor do cateto adjacente:'))
co = float(input('Informe o valor do cateto oposto:'))
print(' CA = {:.2f} e CO = {:.2f}. Sabendo disso, o valor da Hipotenusa é {:.2f}'.format(ca, co, math.hypot(ca, co)))
