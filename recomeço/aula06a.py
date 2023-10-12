n1 = int(input('Digite um número: '))
print(type(n1))
n2 = float(input((' Digite outro número: ')))

s = n1 + n2

#print(' A soma entre', n1, 'e', n2, 'vale', s) Formato antigo do python

print('A soma entre {} e {} vale {}'.format(n1, n2, s))

