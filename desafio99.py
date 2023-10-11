from time import sleep
def maior(* num):
    cont = maior = 0
    print('~~~~~'*10)
    print(f'\n Analisando os valores passados...  ')
    for valor in num:
        print(f'{valor}  ', end='')
        sleep(.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores. ')
    print(f'O maior valor informado foi {maior}')

#PROGRAMA PRINCIPAL
maior(2, 4, 9, 8, 7, 20, 1)
maior(3, 8, 9, 2)
maior(2,1)
maior(0)
