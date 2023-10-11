from time import sleep
def cont(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(.5)
            cont -= p
        print('FIM')


#PROGRAMA PRINCIPAL
cont(1, 10, 1)
cont(10, 0, 2)