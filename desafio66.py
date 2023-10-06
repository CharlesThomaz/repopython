valor = 0
soma = 0
cont = 0
while True:
    valor = int(input('Digite um valor [999 para parar]: '))

    if valor == 999:
        break

    cont = cont + 1
    soma = soma + valor


print(f'A soma dos {cont} valores digitados foi {soma}')
print('FIM')
