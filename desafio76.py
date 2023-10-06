print('=-'*20)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('=-'*20)

tupla = ( 'Lápis', 1.00,
         'Caneta', 2.50,
         'Caderno', 30.00,
         'Mochila', 250.00,
         'Régua', 3.00)

for pos in range(0,  len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos] :.<30}', end='')
    else:
        print(f'R${tupla[pos]:>7.2f}')
print('=-'*20)
