d = float(input('Digite a distância de sua viagem: '))
if d <= 200:
    print('Distância: {}Km'.format(d))
    print('Preço da Passagem: R${:.2f}'.format(d * 0.50))
else:
    print('Distância: {}Km'.format(d))
    print('Preço da Passagem: R${:.2f}'.format(d * 0.45))