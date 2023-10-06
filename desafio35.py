print('_=_' * 10)
print('Analisando triângulo')
print('_=_' * 10)
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
v3 = float(input('Digite o terceiro valor: '))
if v1 < v2+v3 and v2 < v1+v3 and v3 < v1 +v2:
    print ('Os valores acima podem formar triângulos')
else:
    print('Os valores acima não podem formar triângulos')

