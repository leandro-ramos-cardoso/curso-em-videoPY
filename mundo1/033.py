a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

if a > b and a > c:
    print('O maior valor digitado foi {}.'.format(a))
if b > a and b > c:
    print('O maior valor digitado foi {}.'.format(b))
if c > a and c > b:
    print('O maior valor digitado foi {}.'.format(c))

if a < b and a < c:
    print('O menor valor digitado foi {}.'.format(a))
if b < a and b < c:
    print('O menor valor digitado foi {}.'.format(b))
if c < a and c < b:
    print('O menor valor digitado foi {}.'.format(c))