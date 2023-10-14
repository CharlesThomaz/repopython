num = int(input('Digite um número: '))

unidade = num % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = num // 1000
print('Analisando o número {}'.format(num))
print('A unidade é {}'.format(unidade))
print('A dezena é {}'.format(dezena))
print('A centena é {}'.format(centena))
print('O milhar é {}'.format(milhar))
