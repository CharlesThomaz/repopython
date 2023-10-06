print('-=-'*12)
print('CADASTRE UMA PESSOA')
print('-=-'*12)
total = 0
homem = 0
mulher = 0
maior = 0
menor = 0

while True:

    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
        
    print('-=-' * 12)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

    print('-=-' * 12)

    total = total + 1

    if sexo == 'M':
        homem = homem + 1
    if sexo == 'F':
        mulher = mulher + 1

    if idade < 20 and sexo == 'F':
        menor = menor + 1
    if idade > 18:
        maior = maior + 1


print(f'{total} pessoas foram cadastradas, {maior} com mais de 18 anos.')
print(f'{homem} homens foram cadastrados.')
print(f'Dentre as {mulher} mulheres cadastradas, {menor} tem menos de 20 anos.')



