num = 0
opção = 'S'
contador = 0
media = 0
maior = 0
menor = 0
while opção == 'S':
    num = int(input('Digite um número: '))
    opção = str(input('Quer continuar [S/N]? ').upper().strip())
    contador = contador +1
    media = media + num / 2
    if num > maior:
        maior = num
    if num < maior:
        menor = num
print('O maior é {} e o menor é {}'.format(maior, menor))
print('Você digitou {} números e a média deles é: {} '.format(contador, media))
print("OBRIGADO")
