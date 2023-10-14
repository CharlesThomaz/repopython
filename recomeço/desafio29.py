velocidade = int(input('Digite a velocidade do carro?Km/h  '))

if velocidade > 80:
    acima = velocidade - 80
    pagar = acima * 7
    print('Você foi multado!!!')
    print('Você ultrapassou {}km/h acima do limite permitido\nVai pagar um valor de R${}'.format(acima, pagar))
print('TENHA UMA ÓTIMA VIAJEM!!!')