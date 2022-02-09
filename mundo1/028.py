import random
import time
l = [1, 2, 3, 4, 5]
s = random.choice(l) # ESCOLHENDO ALEATORIAMENTE
num = int(input('Digite um número: '))
print('PROCESSANDO ....')
time.sleep(2) # DÁ UM LOADING NO PROGRAMA
if num == s:
    print('PARABENS VOCÊ VENCEU!')
    print('NUMERO ESCOLHIDO POR VOCÊ: {}.'.format(num))
    print('NUMERO ESCOLHIDO PELO PC: {}.'.format(s))
else:
    print('VOCÊ PERDEU!!')
    print('NUMERO ESCOLHIDO POR VOCÊ: {}.'.format(num))
    print('NUMERO ESCOLHIDO PELO PC: {}.'.format(s))