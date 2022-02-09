l = float(input('Informe a largura da parede: '))
a = float(input('Informe a altura da parede: '))
print('A parede mede {} x {} e sua area vale {}m.'.format(l, a, l * a))
print('Para pintar essa parede você vai precisar de {:.2f}L.'.format((l * a)/2))
