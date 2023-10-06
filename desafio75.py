
n = 1
num = (int(input(f'Digite o {n}º valor: ')), int(input(f'Digite o {n+1}º valor: ')),
        int(input(f'Digite o {n+2}º valor: ')), int(input(f'Digite o {n+3}º valor: ')))
print(num)
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}')
else:
    print(f'O valor não apareceu na tupla {num.index}')
print('Os valores pares digitados foram:  ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')




