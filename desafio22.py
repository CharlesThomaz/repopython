nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em Maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
# Contar o número de letras no nome
num_letras = sum(1 for letra in nome if letra.isalpha())
print('Seu nome tem ao todo {} letras'.format(num_letras))
