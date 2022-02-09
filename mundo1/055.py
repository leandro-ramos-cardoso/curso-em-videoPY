"""
DESAFIO 055: Maior e Menor da Sequência
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = 0
menor = -10
for c in range(0, 7):
    peso = float(input('Informe o peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(maior)
print(menor)
