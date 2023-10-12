n = float(input('Digite o perço do produto:R$ '))
desc = n * (5/100)
preco = n - desc
print('O valor a ser pago com 5% de desconto pelo produto é R${}'.format(preco))
