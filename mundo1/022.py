nome = str(input('Informe o nome completo: '))
dividido = nome.split()
quantidade = len(nome)
espaço = nome.count(' ')
print('')
print('ESTUDO COM STRING')
print('='*45)
print('MAIUSCULO: {}'.format(nome.upper()))
print('MINUSCULO: {}'.format(nome.lower()))
print('QUANTIDADE COM ESPAÇOS: {}'.format(quantidade))
print('QUANTIDADE SEM ESPAÇOS: {}'.format(quantidade - espaço))
print('QUANTIDADE DE ESPAÇOS: {}'.format(espaço))
print('QUANTAS LETRAS O 1°: {}'.format(len(dividido[0])))
print('='*45)