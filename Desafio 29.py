v = float(input('Informe a velocidade que o veículo estava:'))
if v > 80:
    x = v - 80
    y = x * 7.00
    print('Você foi multado! Você estava a {} km e pagará de multa pelos km a mais excedidos R${:.2f}'.format(v, y))
else:
    print('Velocidade dentro da quilometragem permitida!')
