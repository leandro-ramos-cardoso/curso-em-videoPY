"""
DESAFIO 043: Índice de Massa Corporal
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('IMC: {:.1f}'.format(imc))
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.1f}'.format(imc))
    print('Peso ideal.')
elif imc >= 25 and imc < 30:
    print('IMC: {:.1f}'.format(imc))
    print('Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('IMC: {:.1f}'.format(imc))
    print('Obesidade.')
else:
    print('IMC: {:.1f}'.format(imc))
    print('Obesidade Mórbida.')