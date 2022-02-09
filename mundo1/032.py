print('\33[1;32mMAIOR E MENOR\33[m')
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
if num1 > num2 and num1 > num3:
    print('O maior valor é {}.'.format(num1))
if num2 > num1 and num2 > num3:
    print('O maior valor é {}.'.format(num2))
if num3 > num1 and num3 > num2:
    print('O maior valor é {}.'.format(num3))

if num1 < num2 and num1 < num3:
    print('O menor valor é {}.'.format(num1))
if num2 < num1 and num2 < num3:
    print('O menor valor é {}.'.format(num2))
if num3 < num1 and num3 < num2:
    print('O menor valor é {}.'.format(num3))