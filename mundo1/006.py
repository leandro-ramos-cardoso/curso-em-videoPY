num = int(input('Digite um número: '))
print('\33[1;31mDOBRO de {} vale {}.\33[m'.format(num, num * 2))
print('\33[1;35mTRIPLO de {} vale {}.\33[m'.format(num, num * 3))
print('\33[1;32mRAIZ QUADRADA de {} vale {:.0f}\33[m.'.format(num, num ** (1/2)))