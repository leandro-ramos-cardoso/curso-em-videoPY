'''num = str(input('Digite um número de 0 a 9999: '))
print('UNIDADE: {}'.format(num[3]))
print('DEZENA: {}'.format(num[2]))
print('CENTENA: {}'.format(num[1]))
print('MILHAR: {}'.format(num[0]))

#REFAZER'''
num = int(input('Digite um número: '))
un = (num // 1) % 10
de = (num // 10) % 10
ce = (num // 100) % 10
mi = (num // 1000) % 10
print('UNIDADE: {}'.format(un))
print('DEZENA: {}'.format(de))
print('CENTENA: {}'.format(ce))
print('MILHAR: {}'.format(mi))
