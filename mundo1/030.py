print('\33[1;30mPASSAGEM ON-LINE\33[m')
d = float(input('Qual a distância da viagem? '))
if d <= 200:
    print('A sua viagem é de {}Km.'.format(d))
    print('Preço: RS{:.2f}'.format(d * 0.50))
else:
    print('A sua viagem é de {}Km'.format(d))
    print('Preço: RS{:.2f}'.format(d * 0.45))