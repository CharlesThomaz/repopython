h = int(input('Qual a altura da parede que deseja pintar?'))
l = int(input('Qual a largura?'))
atotal = h * l
qtdefinal = (atotal * 1)/2
print (' A área total é {}m2 e você precisará de {} litros de tinta para pintar tudo'.format(atotal, qtdefinal))