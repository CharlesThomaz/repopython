from random import choice

a = str(input('Digite um nome: '))
b = str(input('Digite um nome: '))
c = str(input('Digite um nome: '))
d = str(input('Digite um nome: '))

nomes = [a, b, c, d]
escolhido = choice(nomes)

print("O nome selecionado aleatoriamente é: {}".format(escolhido))
