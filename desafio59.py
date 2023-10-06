from time import sleep
menu = 0

num1 = int(input('Digite um nùmero: '))
num2 = int(input('Digite outro número: '))
while menu != 5:
    print('''>>> Escolha a opção desejada: 
[ 1 ]somar  
[ 2 ] multiplicar 
[ 3 ] maior 
[ 4 ] novos números 
[ 5 ] sair do programa ''')
    menu = int(input(' Digite sua opção:'))

    if menu == 1:
        soma = num1 + num2
        print('A soma é {}'. format(soma))
        print('-=-' * 10)
    elif menu == 2:
        multiplicar = num1 * num2
        print('A multiplicação é {}'.format(multiplicar))
        print('-=-' * 10)
    elif menu == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('{} é o número maior.'.format(maior))
        print('-=-' * 10)
    elif menu == 4:
        print('Informe os novos números.')
        num1 = int(input('Digite um nùmero: '))
        num2 = int(input('Digite outro número: '))
    elif menu == 5:
        print('FINALIZANDO...')
    else:
        print(' Digite sua opção: ')
    sleep(2)
print('Programa encerrado com sucesso! OBRIGADO')