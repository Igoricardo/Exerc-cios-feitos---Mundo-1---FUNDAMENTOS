nome = str(input('Digite uma frase:')).strip().lower()
print("""> A letra A aparece {}\n> A 1° letra A apareceu na posição {}\n> E a última letra apareceu na posição {}"""
      .format(nome.count('a'), nome.find('a'), nome.rfind('a')))
