print('\33[1;31mDISSECANDO VARIÁVEIS\33[m')
print('\33[1;31m=\33[m'*20)
p = str(input('Digite algo: '))
print('\33[1;33mO tipo primitivo desse valor é\33[m \33[1;30m{}\33[m'.format(type(p)))
print('Só tem espaços? {}'.format(p.isspace()))
print('É um número? {}'.format(p.isnumeric()))
print('É alfabético? {}'.format(p.isalpha()))
print('É alfanumérico? {}'.format(p.isalnum()))
print('Está em maiúsculas? {}'.format(p.isupper()))
print('Está em minúsculas? {}'.format(p.islower()))
print('Está capitalizada? {}'.format(p.istitle()))