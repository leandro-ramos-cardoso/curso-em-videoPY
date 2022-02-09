salario = float(input('Informe o salario do funcionário: R$'))
print('O salário do funcionário era R${} e com o reajuste ficou R${:.2f}.'.format(salario, salario + (salario * 0.15)))