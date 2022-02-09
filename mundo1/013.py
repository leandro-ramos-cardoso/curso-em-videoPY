salario = float(input('SALÁRIO: R$'))
aumento = salario + (salario + 0.15)
print('{}AUMENTO:{} R${}'.format('\33[1;31m','\33[m',aumento))