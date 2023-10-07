lista = []
cont = 0
while True:
    nome = (str(input('Nome: ')))
    n1 = (float(input('Nota 1: ')))
    n2 = (float(input('Nota 2: ')))
    media = (n1 + n2)/2
    lista.append([nome, [n1,n2], media])
    cont += 1

    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        if continuar in ('S', 'N'):
            break
        else:
            print('Resposta inválida. Por favor, digite S para Sim ou N para Não.')

    if continuar == 'N':
        break


print('_______________'*5)
print(f'{"Nº.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('_______________'*5)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('_______________' * 5)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print(('FINALIZANDO...'))
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('VOLTE SEMPRE')