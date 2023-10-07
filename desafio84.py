temp = []
princ = []
total = 0
maior = 0
menor = 0

while True:
    temp.append(input('Digite seu nome: '))
    temp.append(float(input('Digite seu peso: ')))
    if len(princ) == 0:
       maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    total = total+1
    princ.append(temp[:])
    temp.clear()


    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        if continuar in ('S', 'N'):
            break
        else:
            print('Resposta inválida. Por favor, digite S para Sim ou N para Não.')

    if continuar == 'N':
        break

print('==='*15)
if total <=1:
    print(f'No total foi {total} pessoa cadastrada')
else:
    print(f'No total foram {total} pessoas cadastradas')

print('==='*15)
print('Esses foram as pessoas cadastradas.')
for c in princ:
    print(f'{c[0]} tem {c[1]}kg')
print('==='*15)

print(f'O maior peso foi de [{maior}] kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]. ',)
print(f'O menor peso foi de [{menor}] kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]. ')
print('==='*15)



