from random import shuffle
a1 = input('Digite o primeiro nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o teceiro nome: ')
a4 = input('Digite o quarto nome: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A sequência de jogadores será:{}'.format(lista))