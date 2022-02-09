"""
DESAFIO 050: Soma dos Pares
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
s = 0
for cont in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        s = s + cont
print('\33[1;31mSoma dos valor pares:\33[m {}'.format(s))