'''Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.'''
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O primeiro valor é maior: {}'.format(num1))
elif num2 > num1:
    print('O segundo valor é maior: {}'.format(num2))
else:
    print('\33[1;35mNão existe valor maior, os dois são iguais!\33[m')
