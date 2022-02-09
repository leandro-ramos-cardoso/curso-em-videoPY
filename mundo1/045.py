"""
DESAFIO 045: Pedra, Papel e Tesoura
Crie um programa que faça o computador jogar Jokenpô com você.

Pedra ganha da tesoura (quebra a tesoura)
Tesoura ganha do papel (corta o papel)
Papel ganha da pedra (embrulha a pedra)
"""
import random
import time
pc = [1, 2, 3]
s = random.choice(pc)
print('=-'*20)
print('JOKENPÔ'.center(40))
print('=-'*20)
print('[1] - PEDRA')
print('[2] - PAPEL')
print('[3] - TESOURA')
op = int(input('Digite sua opção: '))
print('Computador pensando ...')
print()
#time.sleep(2)
if op == 1 and s == 2:
    print('Escolha do Usuário: PEDRA')
    print('Escolha do Computador: PAPEL')
    print('SITUAÇÃO: Você escolheu pedra e ganhou do PC que escolheu papel.')
elif op == 1 and s == 3:
    print('Escolha do Usuário: PEDRA')
    print('Escolha do Computador: TESOURA')
    print('SITUAÇÃO: Você escolheu pedra e ganhou do PC que escolheu tesoura.')
elif op == 2 and s == 1:
    print('Escolha do Usuário: PAPEL')
    print('Escolha do Computador: PEDRA')
    print('SITUAÇÃO: Você escolheu papel e ganhou do PC que escolheu pedra.')
elif op == 2 and s == 3:
    print('Escolha do Usuário: PAPEL')
    print('Escolha do Computador: TESOURA')
    print('SITUAÇÃO: Você escolheu papel e perdeu do PC que escolheu tesoura.')
elif op == 3 and s == 1:
    print('Escolha do Usuário: TESOURA')
    print('Escolha do Computador: PEDRA')
    print('SITUAÇÃO: Você escolheu tesoura e perdeu do PC que escolheu pedra.')
elif op == 3 and s == 2:
    print('Escolha do Usuário: TESOURA')
    print('Escolha do Computador: PAPEL')
    print('SITUAÇÃO: Você escolheu tesoura e ganhou do PC que escolheu papel.')
elif op == s:
    print('NINGUEM GANHOU, EMPATOU!')
else:
    print('OPÇÃO INVALIDA !!!')