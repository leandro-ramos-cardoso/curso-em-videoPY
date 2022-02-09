print('SISTEMA DE DESCONTO')
valor = float(input('VALOR DO PRODUTO: R$'))
print('VALOR COM DESCONTO DE 5%:{} R${:.2f}'.format('\33[1;31m',valor - valor * 0.05))