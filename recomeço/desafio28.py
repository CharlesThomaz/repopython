from random import randint
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
num = randint(0,6)
resp = int(input('Em que número pensei? '))
if resp == num:
    print('Acertou!!!')
else:
    print('ERROU!!! Pensei no número {}'.format(num))