"""
DESAFIO 051: Progressão Aritmética
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
pt = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
#fim = int(input('Digite a quantidade de numeros que deseja: '))
decimo = pt + (10 - 1) * r
for c in range(pt, decimo + 2, r):
    print(c)