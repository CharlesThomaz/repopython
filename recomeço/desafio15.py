dias = int(input('Quantos dias alugado? '))
t1 = dias*60
km = int(input('Quantos km rodados? '))
t2 = km*0.15
pagar = t1 + t2
print('O valor a ser pago é R${}.\nReferentes a {}dias e {}km'.format(pagar, dias, km))
