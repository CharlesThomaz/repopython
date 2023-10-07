'''valores = []
par = []
impar = []
for c in range(1,8):
    valores.append(int(input(f'Digite o {c}º valor: ')))
for s in valores:
    if s % 2 == 0:
      par.append(s)
    else:
        if s % 2 == 1:
            impar.append(s)
print(valores)
par.sort()
print(f'Os valores pares são: {par}')
impar.sort()
print(f'Os valores impares são: {impar}')'''

valores = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
      valores[0].append(valor)
    else:
        if valor % 2 == 1:
            valores[1].append(valor)
print(f'Todos os valores são: {valores}')
valores[0].sort()
print(f'Os valores pares são: {valores[0]}')
valores[1].sort()
print(f'Os valores impares são: {valores[1]}')