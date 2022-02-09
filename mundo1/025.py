frase = str(input('Digite uma frase: ')).strip()
q = frase.upper().count('A')
p = frase.upper().find('A') + 1
u = frase.upper().rfind('A') + 1

print('QUANTAS VEZES APARECE A LETRA "A": {}'.format(q))
print('POSIÇÃO EM QUE O "A" APARECE PELA 1º VEZ: {}'.format(p))
print('POSIÇÃO EM QUE O "A" APARECE POR ULTIMO: {}'.format(u))
