"""
DESAFIO 048: Soma Ímpares Múltiplos de Três
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
'''s = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        if c >= 1 and c <= 500:
            s = s + c
            print(c)
print('Soma dos números impares: {}'.format(s))'''
s = 0 #ACUMULADOR - SOMA VALORES
cont = 0 #CONTADOR - CONTA MAIS 1
for n in range(1, 501, 2):
    if n % 3 == 0:
        s = s + n #OU S += N
        cont = cont + 1 #OU CONT += 1
print('TOTAL DOS {} VALORES: {}'.format(cont, s))

