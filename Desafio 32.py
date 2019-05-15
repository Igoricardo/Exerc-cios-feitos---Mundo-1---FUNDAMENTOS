from datetime import date
ano = int(input('Informe o ano ou digite 0  para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 2 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é um ano BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é um ano BISSEXTO!'.format(ano))
