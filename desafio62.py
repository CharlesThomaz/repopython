print('Gerador de PA')
print('-=-'* 10)
num = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo = termo + razão
        cont = cont + 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados'.format(total))
