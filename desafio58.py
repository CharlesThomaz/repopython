from random import randint
computador = randint(0,10)
print('Pensei em um número entre 0 e 10.' )
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Diga qual é o numero?'))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente de novo.')
        elif jogador > computador:
            print('Menos ... tente de novo.')
print('Acertou com {} palpites!'.format(palpites))



