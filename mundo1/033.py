salario = float(input('Informe o salário do funcionário: R$'))
if salario > 1250:
    print('\33[1;30mSalário sem aumento: R${:.2f}\33[m'.format(salario))
    print('\33[1;30mSalário com aumento de 10% R${:.2f}\33[m'.format(salario + (salario * 0.1)))
else:
    print('\33[1;32mSalário sem aumento: R${:.2f}\33[m'.format(salario))
    print('\33[1;32mSalário com aumento de 10% R${:.2f}\33[m'.format(salario + (salario * 0.15)))