n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n

print(f'A soma vale {s:20}')#PYTHON 3.6+
print('A soma vale {}'.format(s))#PYTHON 3
