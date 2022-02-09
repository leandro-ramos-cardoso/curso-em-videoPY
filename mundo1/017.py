import math
print('\33[1;31mCALCULO DA HIPOTENUSA\33[m')
ca = int(input('CATETO ADJCENTE: '))
co = int(input('CATETO OPOSTO: '))
print('HIPOTENUSA: {}'.format(math.hypot(ca, co)))