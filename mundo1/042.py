s1 = int(input('Primeiro Segmento: '))
s2 = int(input('Segundo Segmento: '))
s3 = int(input('Terceiro Segmento: '))
if s1 < s2 + s3 and s1 > abs(s2 - s3):
    print('Pode formar um triangulo.')
    if s1 == s2 == s3:
        print('TIPO DE TRIANGULO: Equilátero.')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('TIPO DE TRIANGULO: Isósceles.')
    elif s1 != s2 != s3:
        print('TIPO DE TRIANGULO: Escaleno.')
else:
    print('Não pode formar um triangulo.')