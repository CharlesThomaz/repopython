media = 0
maioridadehomem = 0
nomevelho = 0
totalmulher = 0
for c in range(1, 5):
    print('----  {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    media = media + idade / 4

    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher = totalmulher + 1

print('Ao todo são {} mulheres com menos de 20 anos'.format(totalmulher))
print('A maior idade  entre os homens é {} e pertence a {}'.format(maioridadehomem, nomevelho))
print('A média das idades é {}'.format(media))




