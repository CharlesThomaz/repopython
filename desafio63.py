print('___'*8)
print(('SEQUÊNCIA DE FIBONACCI'))
print('___'*8)
num = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print('___'*8)

print ('{} - > {}'.format(t1, t2), end=' ')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(' - > {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' -> FIM')
print('___'*8)

