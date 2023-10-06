lista = []
par = []
impar = []

while True:

    n = int(input('Digite um número: '))
    lista.append(n)

    if n % 2 == 0:
        par.append(n)

    elif n % 2 == 1:
        impar.append(n)

    continuar = str(input('Quer continuar: [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'A sua lista completa é: {lista}')
print(f'Os números pares são: {par}')
print(f'O números impares são:{impar}')