from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0,2)

print('{:=^40}'.format('  VAMOS JOGAR O JOGUINHO  '))
print("-"*50)
print('''Escolha uma das opções e digite o número:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
print("-"*50)
jogador = int(input('Qual é a sua jogada?'))
print("_"*50)
print('\033[1;30;41mPedra\033[m...', end='')
sleep(1)
print('\033[1;30;41mpapel\033[m...', end='')
sleep(1)
print('\033[1;30;41mtesoooooooouuuuuuuu\033[m...', end='')
sleep(2)
sleep(1)
print('...\033[1;30;41mra\033[m!!!')
print("_"*50)
print('COMPUTADOR jogou:  \033[1;30;43m{}\033[m'.format(itens[pc]))

print('VOCÊ jogou:  \033[1;30;42m{}\033[m'.format(itens[jogador]))
print("-"*50)
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU!!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!!')
    else:
        print('Jogada inválida!')
elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU!!!')
    else:
        print('Jogada inválida!')

elif pc == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida!')
print("_"*50)