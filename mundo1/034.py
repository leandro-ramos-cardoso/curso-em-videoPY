salario = float(input('Digite o salário R$: '))
if salario > 1250:
    print('Salário: {:.2f}'.format(salario))
    print('Salário com aumento de 10%: {:.2f}'.format(salario + salario * 0.1))
else:
    print('Salário: {:.2f}'.format(salario))
    print('Salário com aumento de 15%: {:.2f}'.format(salario + salario * 0.15))

