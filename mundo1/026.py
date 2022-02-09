nome = str(input('Digite seu nome: ')).strip()
print('\33[1;32mSEPARANDO NOME\33[m')
p = nome.split()[0]
u = nome.split()
print(p)
print(u[len(u) - 1])
