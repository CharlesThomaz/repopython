from random import randint
from time import sleep
num = []
cont = 1
print('=-='*15)
print('          Palpites da MEGA SENA      ')
print('=-='*15)

vezes = int(input('Quantos jogos você quer sortear: '))
for i in range(0, vezes):
    for c in range(0, 5):
        num.append(randint(1, 60))

    print(f'Jogo {cont} : {num:}:')
    cont += 1
    num.clear()
    sleep(1)
print(('=-='*5), 'BOA SORTE', ('=-='*5))
