num = int(input('Digite um número entre 0 e 9999: '))
u = (num // 1) % 10
c = (num // 10) % 10
d = (num // 100) % 10
m = (num // 1000) % 10
print('\33[1;31mMILHAR:\33[m {}'.format(m))
print('\33[1;32mCENTENA:\33[m {}'.format(c))
print('\33[1;33mDEZENA:\33[m {}'.format(d))
print('\33[1;34mUNIDADE:\33[m {}'.format(u))
