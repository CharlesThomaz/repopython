print('Gerador de PA')
print('-=-'* 10)
num = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = num
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end=' ')
    termo = termo + razão
    cont = cont + 1
print('FIM!!!')
