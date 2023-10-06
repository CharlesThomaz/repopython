print('{:=^40}'.format(' LOJAS DO CHARLÃO '))
preco = float(input('Valor da compra:R$ '))
pagamento = int(input(''' Formas de pagamento:
[ 1 ] Para pagamento a vista ou cheque
[ 2 ] Para pagamento à vista no cartão
[ 3 ] Para pagamento em até 2x no cartão
[ 4 ] Para pagamento em 3x ou mais no cartão
Digite a opção: '''))
if pagamento == 1:
    total = preco - (preco * 10/100)
    print('O preço a ser pago pelo produto é R${}'.format(total))
elif pagamento == 2:
    total = preco - (preco * 5/100)
    print('O preço a ser pago pelo produto é R${:.2f}'.format(total))
elif pagamento == 3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x sem juros de R${}'.format(parcela))
elif pagamento == 4:
    total = preco + (preco * 20/100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcelas = total / total_parcelas
    print('Sua compra será parcela com juros em {}x de R${} ' .format(total_parcelas, parcelas))
else:
    total = 0
    print('Opção inválidade de pagamento!TENTE NOVAMENTE!')




