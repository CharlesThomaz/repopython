temp = []
princ = []
total = 0

while True:
    temp.append(input('Digite seu nome: '))
    temp.append(float(input('Digite seu peso: ')))
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
print('Esses foram os cadastrados.')
for c in princ:
    print(f'{c[0]} tem {c[1]}kg')
    a



