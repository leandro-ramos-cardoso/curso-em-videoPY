num = int(input('\33[1;35mMe diga um número qualquer: \33[m'))
if num %2 == 0:
    print('\33[1;32mO número {} é PAR.\33[m'.format(num))
else:
    print('\33[1;31mO número {} é IMPAR.\33[m'.format(num))