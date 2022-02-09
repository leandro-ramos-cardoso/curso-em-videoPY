"""
DESAFIO 054: Grupo de Maioridade
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
totmenor = 0
totmaior = 0
atual = date.today().year
for c in range(1, 8):
    dn = int(input('Informe o ano de nascimento: '))
    idade = atual - dn
    if idade < 18:
        totmenor = totmenor + 1
    else:
        totmaior = totmaior + 1
print('Quantidade de pessoas de maior: {}'.format(totmaior))
print('Quantidade de pessoas de menor: {}'.format(totmenor))
