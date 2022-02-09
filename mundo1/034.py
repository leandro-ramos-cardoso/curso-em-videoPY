seg1 = float(input('Primeiro Segmento: '))
seg2 = float(input('Segundo Segmento: '))
seg3 = float(input('Terceiro Segmento: '))
if abs(seg1 - seg2) < seg3 < (seg1 + seg2):
    print('\33[1;32mOs segmentos acima PODEM FORMAR UM TRIÂNGULO.\33[m')
else:
    print('\33[1;31mOs segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO.\33[m')