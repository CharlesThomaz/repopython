print('=*='*20)
print('{:^60}'.format('---THOMAZ BANK---'))
print('=*='*20)
valor = int(input('Qual o valor você quer sacar ? R$ '))
total = valor
céd = 50
totcéd = 0

while True:
    if total >= céd:
       total = total - céd
       totcéd = totcéd + 1
    else:
        if totcéd > 0:
            print(f'Você receberá {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break

print('=*='*20)
print('OBRIGADO POR UTLIZAR NOSSOS SERVIÇOS! VOLTE SEMPRE!')