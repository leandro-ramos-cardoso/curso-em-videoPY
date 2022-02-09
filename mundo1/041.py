"""
DESAFIO 041: Classificando Atletas
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""
import time
an = int(input('Informe o ano nascimento: '))
at = int(time.strftime('%Y'))
idade = at - an
if idade <= 9:
    print('IDADE: {}'.format(idade))
    print('CATEGORIA: Mirim')
elif idade > 9 and idade <= 14:
    print(('IDADE: {}'.format(idade)))
    print('CATEGORIA: Infantil')
elif idade > 14 and idade <= 19:
    print('IDADE: {}'.format(idade))
    print('CATEGORIA: Junior')
elif idade > 19 and idade <= 25:
    print('IDADE: {}'.format(idade))
    print('CATEGORIA: Sênior')
else:
    print('IDADE: {}'.format(idade))
    print('CATEGORIA: Master')