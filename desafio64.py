soma = 0
contador = 0
n1 = 0
n1 = int(input('Digite um número[999 PARA PARAR]:'))
while n1 != 999:
    soma = soma + n1
    contador = contador + 1
    n1 = int(input('Digite um número[999 PARA PARAR]:'))


print('Vocé digitou {} números'.format(contador))
print('A SOMA FOI {}'.format(soma))