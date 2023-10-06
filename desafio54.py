from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    ano = int(input('Em que ano nasceu a {}ª pessoa? '.format(c)))
    idade = atual - ano + 1
    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print('Temos {} maior de idade e {} menores'.format(totalmaior, totalmenor))

