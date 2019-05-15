salario = float(input("Informe o seu salário: R$"))
if salario >= 1250:
    ns = salario + (salario * 10/100)
else:
    ns = salario + (salario * 15/100)
print('Seu salário informado foi R${:.2f}, desta forma seu novo salário depois do aumento é R${:.2f}'.format(salario, ns))