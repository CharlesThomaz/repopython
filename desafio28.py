from random import randint
from time import sleep
pc = randint(0,5) #Faz o pc "PENSAR"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente dizer qual é o número...')
print('-=-'*20)
jogador = int(input('Em que número pensei?'))#Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == pc:
    print('PARABÉNS! Você brilhou.')
else:
    print('Que pena. Eu pensei no número {} e não no número {}!Tente de novo.' .format(pc, jogador))


