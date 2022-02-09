km = float(input('Quantos KM percorridos? '))
dias = int(input('Quantos dias alugados? '))
print('='*20)
print('Km rodados: {}km.'.format(km))
print('Dias alugado: {} dias.'.format(dias))
print('Preço a pagar: R${:.2f}.'.format((dias * 60) + (km * 0.15)))


#Exercício Python 015: Escreva um programa que pergunte a
# quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.