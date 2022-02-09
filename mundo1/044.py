"""
DESAFIO 044: Gerenciador de Pagamentos
Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
precon = float(input('Informe o preço do produto: '))
print('[1] - À VISTA NO DINHEIRO')
print('[2] - À VISTA NO CHEQUE')
print('[3] - À VISTA NO CARTÃO')
print('[4] - EM 2x NO CARTÃO')
print('[5] - EM 3x ou mais no CARTÃO')
cond_p = int(input('Qual a condição de pagamento? '))
if cond_p == 1 or cond_p == 2:
    print()
    print('Preço Normal: {}'.format(precon))
    print('Com 10% de desconto: {}'.format(precon - (precon * 0.1)))
elif cond_p == 3:
    print()
    print('Preço Normal: {}'.format(precon))
    print('Com 5% de desconto: {}'.format(precon - (precon * 0.05)))
elif cond_p == 4:
    print()
    p = int(input('Em quantas parcelas? '))
    if p <= 2:
        print()
        print('Preço Normal: {}'.format(precon))
    else:
        print()
        print('Preço Normal: {}'.format(precon))
        print('Aumento de 20% de juros: {}'.format(precon + (precon * 0.2)))
else:
    print('\33[1;31mOPÇÃO INVALIDA!!!\33[m')