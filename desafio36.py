valor_casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$ '))
anos_pagamento = int(input('Em quantos anos irá pagar? '))
valor_parcelas = valor_casa / (anos_pagamento * 12)
print('O valor das parcelas a ser pago durante {} anos é R${:.2f}'.format(anos_pagamento, valor_parcelas))
porcento = salario * (30/100)
if valor_parcelas >= porcento:
    print ('Empréstimo negado.')
else:
    print('Seu empréstimo foi aprovado.')

print('Obrigado pela preferência.')





