tupla = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
         'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

num = int(input('Digite um número entre 0 e 20: '))

while True:
    while num not in range(0, 21):
        num = int(input('Número fora do intervalo. Digite um número entre 0 e 20: '))

    print(f'Você digitou o número {(tupla[num])}')

    print('-=-'*20)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input(' Quer continuar [S/N] ?')).strip().upper()[0]
   
    if continuar == 'N':
        break
    else:
        print('-=-' * 20)

        num = int(input('Digite um número entre 0 e 20: '))
print('-=-'*20)

print('TCHAU!!')

