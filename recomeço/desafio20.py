from random import shuffle

a = str(input('Digite um nome: '))
b = str(input('Digite um nome: '))
c = str(input('Digite um nome: '))
d = str(input('Digite um nome: '))

nomes = [a, b, c, d]
shuffle(nomes)

print('A ordem das apresentações será:\n{} '.format(nomes))
