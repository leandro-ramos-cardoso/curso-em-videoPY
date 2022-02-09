ano = int(input('\33[1;34mQue ano você quer analisar? \33[m'))
if ano % 4 == 0 and ano % 100 !=0:
    print('ANO BISSEXTO')
else:
    print('ANO NÃO BISSEXTO')