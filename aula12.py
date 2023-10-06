nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Anna' or nome == 'Sarah' or nome == 'Kaleb' or nome == 'Abner':
    print('Esse nome é Bíblico!')
elif nome == 'Charles':
    print('Esse nome é de um Pai de família.')
elif nome == 'Tássia':
    print('Esse nome é de uma mãe de família.')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
