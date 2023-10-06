from  random import choice
a1 = input('Digite o nome de membros da sua família: ')
a2 = input('Digite outro nome: ')
a3 = input('Mais um nome: ')
a4 = input('Só mais um:')
a5 = input('kkk...Outro: ')
a6 = input('Dessa vez é o último: ')
lista = [a1, a2, a3, a4, a5, a6]
sorteio = choice(lista)
print('A pessoa escolhida pra fazer a janta é ===> "{}"'.format(sorteio))