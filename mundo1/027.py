import time
import random
numeros = [1,2,3,4,5]
s = random.choice(numeros)
print('\33[1;33m-=-\33[m'*20)
print('\33[1;34mVou pensar em um número entre 0 e 5. Tente advinhar...\33[m')
print('\33[1;33m-=-\33[m'*20)
num = int(input('Em que número eu pensei? '))
print('\33[1;35mPROCESSANDO...\33[m')
time.sleep(2)
if s == num:
    print('\33[1;32mPARABÉNS! Você conseguiu me vencer!\33[m')
else:
    print('\33[1;31mGANHEI! Eu pensei no número {} e não no {}!\33[m'.format(s, num))
