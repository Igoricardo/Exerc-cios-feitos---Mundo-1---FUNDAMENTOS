km = float(input('Informe quantos KM terá sua viagem: KM '))
if km <= 200:
    v = km * 0.50
else:
    v = km * 0.45
print('O valor da passagem por {} KM que você vai pagar será: R$ {:.2f}'.format(km, v))
