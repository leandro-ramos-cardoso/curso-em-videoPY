nome = str(input('Digite o nome da cidade: ')).upper()
f = 'SANTO' in nome.split()[0]
print('\33[1;33mO nome da cidade começa com SANTO?\33[m {}'.format(f))

