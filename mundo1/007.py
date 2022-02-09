nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print('A média do aluno foi de {}.'.format(media))
if media >= 7:
    print('\33[1;32mAluno Aprovado\33[m')
else:
    print('\33[1;31mAluno Reprovado\33[m')
