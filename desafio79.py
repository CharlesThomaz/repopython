valor = []

while True:


    num = (int(input('Digite um número: ')))
    if num not in valor:
        valor.append(num)
        print('Valor adicionado à lista!')
    else:
        print('Número já existe na lista.')


    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar != 'S' and continuar != 'N':
        print('Opção incorreta. Por favor, digite "S" para continuar ou "N" para sair.')
    else:
        if continuar == 'N':
            break

print('=-'*20)
valor.sort()
print(f'Os valores digitados foram: {valor}')
