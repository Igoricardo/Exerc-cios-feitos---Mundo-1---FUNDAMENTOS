p = float(input('Informe o preço do produto: R$'))
print('O preço do produto = R$ {:.2f}, a loja está oferecendo 5% de desconto, desta forma o novo preço do item é R$ {:.2f}'.format(p, p-(p*5/100)))