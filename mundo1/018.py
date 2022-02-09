import math
angulo = float(input('Digite o ângulo: '))
print('\33[1;31mSENO: {:.2f}\33[m'.format(math.sin(math.radians(angulo))))
print('\33[1;31mCOSSENO: {:.2f}\33[m'.format(math.cos(math.radians(angulo))))
print('\33[1;31mTANGENTE: {:.2f}\33[m'.format(math.tan(math.radians(angulo))))
