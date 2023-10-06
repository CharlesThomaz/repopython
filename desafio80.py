'''lista = []
maior = 0
menor = 0
for item in range(0,5):

    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado.')
        if n > maior:
            maior = n
            print('Valor no final da lista.')
        else:
            if n < menor:
                menor = n
                lista.insert(0, n)
                print('Adicionado no início da lista.')

    else:
        print('Número já exite na lista.')
print(f'Sua lista é: {lista}')'''

lista = []

for item in range(0, 5):
    num = int(input('Digite um valor: '))
    if item == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        n = 0
        while n < len(lista):
            if n <= lista[n]:
                lista.insert(n, num)
                print(f'Adicionado na posicão {n} da lista')
                break
            n = n+1
print(f'Os valores digitados em ordem foram{lista}')



