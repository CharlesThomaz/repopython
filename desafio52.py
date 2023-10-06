n = int(input('Digite um número: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        t = t + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('O numéro {} foi divisivel {} vezes'.format(n, t))
if t == 2:
    print('Por isso ele é PRIMO')
else:
    print('Por isso ele NÃO É PRIMO ')