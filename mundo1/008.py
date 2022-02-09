frase = '\33[1;36;40mCONVERSÃO DE UNIDADES\33[m'
print('')
print(frase.center(50))
print('')
t = int(input('Digite um valor em Metros: '))
print('{}m vale {}cm.'.format(t, t * 100))
print('{}m vale {}mm.'.format(t, t * 1000))