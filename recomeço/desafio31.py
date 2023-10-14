distancia = int(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
if distancia < 200:
    preço = distancia * .50
else:
    preço = distancia * .45

print('O preço da passagem será de R${:.2f}'.format(preço))

