nome = str(input('Digite o nome completo: '))
print('\33[1;33mMAIUSCULAS:\33[m {}'.format(nome.upper()))
print('\33[1;31mMINUSCULAS:\33[m {}'.format(nome.lower()))
espaco = nome.count(' ')
#print(nome.count(' '))
print('\33[1;36mQUANTIDADE DE LETRAS SEM ESPAÇOS:\33[m {}'.format((len(nome) - espaco)))
print('\33[1;34mQUANTIDADE DE LETRAS DO 1º NOME:\33[m {}'.format(len(nome.split()[0])))