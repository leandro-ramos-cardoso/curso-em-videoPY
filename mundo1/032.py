from datetime import date
a = int(input('Digite o ano: '))
if a == 0:
    a = date.today().year # PEGANDO AO ANO ATUAL DA MAQUINA
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Ano Bisexto')
else:
    print('Ano não Bisexto')