print('-=-'*10)
print('{:^30}'.format('LOJÃO DO CHARLÃO'))
print('-=-'*10)
nprodutos = 0
mais1000 = 0
total = 0
menor = 0
contador = 0
barato = ''
while True:
    nome = str(input('PRODUTO: ')).upper().strip()
    preço = float(input('PREÇO: R$ '))
    contador = contador + 1
    total = total + preço
    nprodutos = nprodutos + 1
    print('-=-'*10)
    if preço > 1000:
        mais1000 = mais1000 + 1
    if contador == 1:
        menor = preço
        barato = nome

    else:
        if preço < menor:
            menor = preço

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N] ?')).strip().upper()[0]
    if continuar == 'N':
        break

    print('-=-'*10)




print('-=-'*20)


print(f'{nprodutos} produtos foram comprados dando um total de R${total} ')
print(f'{mais1000} produtos com preço maior que R$1000,00 ')
print(f'O produto mais barato foi {barato} e custa R${menor}')

print('-=-'*20)
print('{:^30}'.format('FIM DO PROGRAMA'))
print('-=-'*10)