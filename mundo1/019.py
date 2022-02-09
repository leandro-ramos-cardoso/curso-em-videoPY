'''import random
print(random.randint(1, 45))'''

import random
a1 = (input('Primeiro aluno: '))
a2 = (input('Segundo aluno: '))
a3 = (input('Terceiro aluno: '))
a4 = (input('Quarto aluno: '))
nome = [a1, a2, a3, a4]
#nome = ['Leandro', 'Kézya', 'Josemir', 'Margarida']
print(random.choice(nome))
