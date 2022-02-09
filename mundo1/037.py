num = int(input('Digite um número: '))
print('CONVERSÃO')
print('[1] - BINÁRIO')
print('[2] - OCTAL')
print('[3] - HEXADECIMAL ')
op = int(input('Escolha a base de conversão: '))
if op == 1:
    print(bin(num)[2:])
elif op == 2:
    print(oct(num)[2:])
elif op == 3:
    print(hex(num)[2:])
else:
    print('\33[1;31mOPÇÃO INVÁLIDA!!!\33[m')
