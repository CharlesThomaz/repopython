p = float(input('Digite o seu peso atual:(Kg) '))
h = float(input('Digite a sua altura: (m) '))
imc = p / ( h ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >=30 and imc < 40:
    print('Obesidade')
elif imc > 40:
    print ("obesidade mórbida")



