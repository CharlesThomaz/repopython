from random import randint

print('-=-'*10)
print('{:^30}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('-=-'*10)
v = 0

while True:
    jogador = int(input('Escolha seu número?'))
    pc = randint(0, 10)
    res = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Seu número foi {jogador} e o do computador foi {pc}', end=' ')
    print('Deu PAR' if res % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if res % 2 == 0:
            print ('Você VENCEU!')
            v = v + 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if res % 2 == 1:
            print('Vocè VENCEU')
            v = v + 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! VOCê VENCEU {v} VEZES')



