print('Olá, Bem vindo ao futuro!!!')
nome = str(input('Digite seu nome: ').upper().strip())

while nome != 'CHARLES':
    nome = str(input('Digite seu nome: ').upper().strip())

print('Bem vindo {}'.format(nome))
