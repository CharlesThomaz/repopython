
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite seu sexo: [M/F]')).strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))

