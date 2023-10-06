distancia = float(input('Digite a distância da viagem:'))
if distancia <= 200:
    preco = distancia * .50
else:
    preco = distancia * .45
print('O valor da viagem será R${:.2f}'.format(preco))
