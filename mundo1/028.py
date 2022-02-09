from datetime import date
print()
print('\33[1;33mDETRAN - PB\33[m'.center(55))
print('\33[1;34m=\33[m'*50)
velo = float(input('\33[1;30mVelocidade do carro: \33[m'))
multa = (velo - 80) * 7
if velo > 80:
    print('\33[1;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h.\33[m')
    print('\33[1;31mKm/h ULTRAPASSADOS: {:.0f}Km/h\33[m'.format(velo - 80))
    print('\33[1;31mVALOR DA MULTA: R${:.2f}\33[m'.format(multa))
else:
    print('\33[1;32mDIGIJA COM CUIDADO. TENHA UM BOM DIA!\33[m')
print('\33[1;34=\33[m'*30)
print()
print('\33[1;30mCabedelo, {}\33[1;30m'.format(date.today()))
print('\33[1;34m=\33[m'*50)