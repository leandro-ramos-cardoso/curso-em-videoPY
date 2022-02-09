cores = {'limpa':'\33[m',
         'branco':'\33[1;30m',
         'azul':'\33[1;34m',
         'azulC':'\33[1;46m',
         'amarelo':'\33[1;33m',
         'vermelho':'\33[1;31m',
         'verde':'\33[1;32m',
         'roxo':'\33[1;35m'}
print()
print('{}{}SIMULADOR HABITACIONAL V.01{}'.format(cores['branco'],cores['azulC'],cores['limpa']).center(66))
print('{}={}'.format(cores['azul'], cores['limpa'])*50)
print('{}-INFORMAÇÕES-{}'.format(cores['roxo'], cores['limpa']))
print()
i = float(input('{}Qual o valor do imóvel?{} {}R${}'.format(cores['branco'], cores['limpa'], cores['amarelo'], cores['limpa'])))
s = float(input('{}Qual o valor do salário?{} {}R${}'.format(cores['branco'], cores['limpa'], cores['amarelo'], cores['limpa'])))
a = int(input('{}Em quantos anos vai pagar?{} '.format(cores['branco'], cores['limpa'])))
#pm = (i / s) * a
pm = i / (a * 12)
if pm > (s * 0.3):
    print('{}EMPRESTIMO NEGADO. VOCÊ NÃO PODE COMPROMETER MAIS QUE 30% DA SUA RENDA!!{}'.format(cores['vermelho'], cores['limpa']))
    #print(pm)
else:
    print('{}PROPOSTA DE EMPRESTIMO ACEITA.{}'.format(cores['verde'], cores['limpa']))
    print('{}Valor da prestação:{} {}RS{:.2f}{}'.format(cores['azul'], cores['limpa'], cores['branco'],pm, cores['limpa']))