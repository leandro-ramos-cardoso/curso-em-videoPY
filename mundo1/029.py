v = float(input('Informe a velocidade do carro: '))
u = v - 80
if v > 80:
    print('=' * 26)
    print('       VELOCIMETRO')
    print('='*26)
    print('Você foi multado!')
    print('Km acima do permitido: {}Km/h'.format(u))
    print('Valor da Multa: R${:.2f}'.format(u * 7))
else:
    print('Tenha um bom dia! Dirija com segurança!')
