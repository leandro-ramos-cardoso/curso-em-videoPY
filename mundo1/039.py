import time
print('\33[1;34m=\33[m'*30)
print('\33[1;30mALISTAMENTO MILITAR\33[m'.center(37))
print('\33[1;34m=\33[m'*30)
print()
ano_nasc = int(input('Informe o ano de nascimento: '))
sexo = str(input('Informe seu sexo: ')).upper()
ano_atual = int(time.strftime('%Y'))
idade = ano_atual - ano_nasc
falta = 18 - idade
passou = idade - 18
if sexo == 'FEMININO':
    print('Você não precisa se alistar.')
elif sexo == 'MASCULINO':
    if idade < 18:
        print('Idade: {}'.format(idade))
        #print('Quanto tempo falta: {} anos.'.format(falta))
        print('\33[1;33mSITUAÇÃO: Falta {} anos para se alistar.\33[m'.format(falta))
        print('Ano para se alistar: {}'.format(ano_nasc + 18))
    elif idade == 18:
        print('Idade: {}'.format(idade))
        print('\33[1;32mSITUAÇÃO: Hora de se alistar.\33[m')
    else:
        print('Idade: {}'.format(idade))
        #print('Quanto tempo já passou: {} anos.'.format(passou))
        print('\33[1;31mSITUAÇÃO: Passou {} anos do tempo do alistamento.\33[m'.format(passou))
        print('Ano para ter se alistado: {}'.format(ano_nasc + 18))