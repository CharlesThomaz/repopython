num = 0
cer = 0
er = 0
print('__' * 15)
print('RESPONDA AS OPERAÇÕES:')
print('__' * 15)

for c in range(0, 10, 2):
    resp = input('{} x {} = '.format(c, c +1))

    if resp.isnumeric():
        resp = int(resp)
    else:
        print('Digite novamente: Não é um número válido.')
        continue


    num += 1

    if c * (c+1) == resp:
        cer += 1
        print('Certo')
        print('Continue acertando.')
        print('__'*10)
        print('')

    else:
        er += 1
        print('Errado')
        print('Vai dar certo continue.')
        print('__'*10)

        print(' ')

print('Foram {} operações'.format(num))
print('Você teve {} acertos e {} erros.'.format(cer, er))
print('FIM')
