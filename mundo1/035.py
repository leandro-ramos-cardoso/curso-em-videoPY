print('-=-'*15)
print('Analisador de Triângulos')
print('-=-'*15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if abs(r2 - r3) < r1 < (r2 + r3):
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo.')
