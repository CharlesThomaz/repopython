salario = float(input('Digite o salário do funcionário:R$ '))
if salario > 1250:
    aumento = ((salario * 10)/100 + salario)
else:
    aumento = ((salario * 15)/100 + salario)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumento))