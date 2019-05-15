x = input('Digite seu nome completo:').strip()
print("""O nome informado foi: {}.
em maiúscula é: {}. 
em minúscula é: {}.
Quantas letras ao todo sem considerar os espaços: {}.""".format(x.title(), x.upper(), x.lower(), len(x.replace(' ', ''))))
separa = x.split()
print('Quantas letras tem o 1° nome: {} letras.'.format(len(separa[0])))


