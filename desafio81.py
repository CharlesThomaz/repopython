lista = []
while True:
    lista.append(int(input('Digite um valor: ')))

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar == 'S':
            break
        if continuar == 'N':
            break

        elif continuar != 'N' and continuar != 'S':
            print('Opção incorreta.')

    if continuar == 'N':
        break


print('___'*12)

if 5 in lista:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado ou não está na lista.')

print(f'Sua lista contém {len(lista)} números')

lista.sort(reverse=True)
print(f'Os valores classificados de maneira decrescente são:{lista}')