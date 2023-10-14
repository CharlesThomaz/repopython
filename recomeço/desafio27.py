nome = str(input('Digite seu nome completo: '))
n = nome.split()
print('Seu nome completo é: {}, \nseu primeiro nome é: {}, \ne seu último nome é: {} '.format(nome, n[0], n[len(n)-1] ))
