nome = str(input('Digite um nome: ')).upper()
teste = 'SILVA' in nome
print('\33[1;31mO nome possui Silva?\33[m {}'.format(teste))