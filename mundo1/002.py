import time
nome = str(input('Informe o seu nome: '))
titulo = 'SISTEMA DE CADASTRO'
print('\33[1;30;44m=-='*15, '\33[m')
print('\33[36m', titulo.center(42))
print('\33[1;30;44m=-='*15, '\33[m')
print('\33[1;31mPROCESSANDO...\33[m')
time.sleep(2)
print('Olá {}{}{}, bem vindo ao nosso sistema.'.format('\33[32m', nome, '\33[m'))